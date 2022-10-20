from setuptools import setup, find_packages

setup(
    name='frida-rpc',
    version='0.0.1',
    packages=find_packages(),
    # packages=find_packages(),
    description='frida rpc',
    long_description='easy to use frida rpc with flask',
    author='Michael Wang',
    author_email='shiqwang@gmail.com',
    license='GPL',
    keywords=['frida', 'fridarpc'],
    platforms='Independant',
    url='http://github.com',
    entry_points={
        'console_scripts': [
            'frida-rpc = fridarpc.run:run',
        ]
    }
)