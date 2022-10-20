import logging

import frida
from flask import Flask, request
import sys, os
from werkzeug.exceptions import MethodNotAllowed

app = Flask(__name__)

script = None

exports_funcs = []


@app.route('/')
def hello():
    return 'hello world'

@app.errorhandler(404)
def e404(error):
    global script, exports_funcs
    export_name = request.path.replace('/', '')
    if export_name in exports_funcs:
        data = request.get_json()
        try:
            # return script._rpc_request('call', export_name, data)
            ret = getattr(script.exports, export_name)(data)
            return ret
        except Exception as e:
            logging.exception(e)
            return 'call error'
    else:
        return f'no export named {export_name}'


def run():
    global script, exports_funcs

    devices = frida.enumerate_devices()

    print(sys.argv)

    for r in devices:
        print('id', r.id, 'name', r.name, 'type', r.type)

    try:
        device = frida.get_device(sys.argv[1])
    except:
        print('no device found')
        exit(0)

    if not os.path.exists(sys.argv[2]):
        print('no js file found')
        exit(0)

    session = device.attach(sys.argv[3])

    with open(sys.argv[2]) as f:
        code = f.read()
    script = session.create_script(code)
    script.load()
    exports_funcs = script.list_exports()
    print('exports:', exports_funcs)
    app.run('0.0.0.0', 5555)



if __name__ == '__main__':
    run()
