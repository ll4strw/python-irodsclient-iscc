import os

__version__ = '0.0.1'

def version_as_string():
    return os.environ.get('PYTHON_IRODSCLIENT_ISCC_VERSION', __version__.strip())

def version_as_tuple():
    return tuple(int(x) for x in version_as_string().split('.'))
