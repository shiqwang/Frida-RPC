import logging

import frida
from flask import Flask, request, jsonify
import sys, os
from werkzeug.exceptions import MethodNotAllowed
from flask_cors import CORS

app = Flask(__name__,
            template_folder='front/dist',
            static_folder='front/dist/static')

CORS(app, resources=r'/*')

script = None

exports_funcs = []

device_rpc_manage = {}


def check_frida_status(device_id):
    return os.path.exists(f'./tmp/{device_id}')


def new_frida_service(device_id):
    with open(f'./tmp/{device_id}', 'w') as f:
        f.write('1')

    # return apps


def check_device_exist(device_id):
    for item in frida.enumerate_devices():
        if item.id == device_id:
            return True
    return False


@app.route('/')
def hello():
    return 'hello world'


@app.errorhandler(404)
def e404(error):
    global device_rpc_manage
    device_id = request.args.get('device_id')
    if device_id not in device_rpc_manage:
        return jsonify({'code': -1, 'msg': 'not running'})
    export_name = request.path.replace('/', '')
    data = request.get_json()
    try:
        # return script._rpc_request('call', export_name, data)
        ret = getattr(device_rpc_manage[device_id]['script'].exports, export_name)(data)
        return ret
    except Exception as e:
        logging.exception(e)
        return 'call error'


@app.route('/admin/frida')
def frida_service():
    device_id = request.args.get('device_id')

    if not check_device_exist(device_id):
        return jsonify({'code': -1, 'msg': 'device not found'})

    if check_frida_status(request.args.get('device_id')):
        return jsonify({'code': -1, 'msg': 'frida is running'})
    else:
        device = frida.get_device(device_id)
        apps = device.enumerate_applications()
        return apps


@app.route('/admin/device_rpc')
def device_rpc():
    global device_rpc_manage
    device_id = request.args.get('device_id')
    if device_id in device_rpc_manage:
        return jsonify({'code': 0, 'data': {'app_id': device_rpc_manage[device_id]['app_id'],
                                            'hook_js': device_rpc_manage[device_id]['hook_js']}})
    else:
        return jsonify({'code': 1, 'msg': 'not running'})


@app.route('/admin/devices')
def admin_devices():
    global device_rpc_manage
    devices = frida.enumerate_devices()
    data = []
    for r in devices:
        if 'Local' in r.name:
            continue
        data.append({
            'name': r.name,
            'id': r.id,
            'type': r.type,
            'is_running': r.id in device_rpc_manage,
            'app_id': device_rpc_manage[r.id]['app_id'] if r.id in device_rpc_manage else None,
            'hook_js': device_rpc_manage[r.id]['hook_js'] if r.id in device_rpc_manage else None
        })
    return jsonify(data)


@app.route('/admin/start')
def start():
    global device_rpc_manage
    device_id = request.args.get('device_id')
    hook_js = request.args.get('hook_js')
    app_id = request.args.get('app_id')
    if check_frida_status(device_id):
        return jsonify({'code': -1, 'msg': 'already running'})
    else:
        device = frida.get_device(device_id)
        session = device.attach(app_id)
        with open(f'resources/hookjs/{hook_js}') as f:
            code = f.read()
        script = session.create_script(code)
        script.load()
        exports = script.list_exports()
        device_rpc_manage[device_id] = {}
        device_rpc_manage[device_id]['script'] = script
        device_rpc_manage[device_id]['session'] = session
        device_rpc_manage[device_id]['hook_js'] = hook_js
        device_rpc_manage[device_id]['app_id'] = app_id
        return jsonify({"code": 0, 'msg': 'ok'})


@app.route('/admin/stop')
def stop_rpc():
    global device_rpc_manage
    device_id = request.args.get('device_id')
    del device_rpc_manage[device_id]
    return jsonify({'code': 0})


@app.route('/admin/apps')
def apps():
    device_id = request.args.get('device_id')
    try:
        device = frida.get_device(device_id)
        apps = device.enumerate_applications()
        data = []
        for r in apps:
            if r.pid == 0:
                continue
            data.append({
                'id': r.identifier,
                'name': r.name,
                'pid': r.pid
            })
        return jsonify(data)
    except:
        pass


@app.route('/admin/hookjs')
def hook_js():
    file_list = os.listdir('resources/hookjs')
    return file_list


@app.route('/admin/apks')
def apk_list():
    file_list = os.listdir('resources/apk')
    return file_list


@app.route('/admin/rpc_list')
def rpc_list():
    global device_rpc_manage
    device_id = request.args.get('device_id')
    data = {}
    if not device_id:
        for r in device_rpc_manage:
            data[r] = device_rpc_manage[r]['script'].list_exports()
    else:
        data[device_id] = device_rpc_manage[device_id]['script'].list_exports()
    return data



def run():
    # global script, exports_funcs
    #
    # devices = frida.enumerate_devices()
    #
    # print(sys.argv)
    #
    # for r in devices:
    #     print('id', r.id, 'name', r.name, 'type', r.type)
    #
    # try:
    #     device = frida.get_device(sys.argv[1])
    # except:
    #     print('no device found')
    #     exit(0)
    #
    # if not os.path.exists(sys.argv[2]):
    #     print('no js file found')
    #     exit(0)
    #
    # try:
    #     session = device.attach(sys.argv[3])
    # except Exception as e:
    #     logging.exception(e)
    #     print('no process found')
    #     exit(0)
    #
    # with open(sys.argv[2]) as f:
    #     code = f.read()
    # script = session.create_script(code)
    # script.load()
    # exports_funcs = script.list_exports()
    # print('exports:', exports_funcs)
    app.run('0.0.0.0', 5555, debug=True)


if __name__ == '__main__':
    run()
