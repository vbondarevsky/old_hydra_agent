import platform
import subprocess
from locale import getpreferredencoding
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


def run_command(args):
    r = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True, check=True)
    return r.stdout.strip()
