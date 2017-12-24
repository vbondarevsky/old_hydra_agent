import platform
import subprocess
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
    r = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return_code, out, err = r.returncode, r.stdout.decode().strip(), r.stderr.decode().strip()

    if return_code:
        raise Exception(err)
    else:
        return out
