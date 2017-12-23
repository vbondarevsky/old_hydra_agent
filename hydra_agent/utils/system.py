import platform
from tempfile import NamedTemporaryFile


def is_linux():
    return platform.system() == 'Linux'


def is_windows():
    return platform.system() == 'Windows'


def is_mac():
    return platform.system() == 'Darwin'


def temp_file_name():
    with NamedTemporaryFile(delete=False) as tmp:
        return tmp.name
