import subprocess


def success_result(args, out):
    return subprocess.CompletedProcess(args, 0, out, '')


def fail_result(args, return_code, out, err=''):
    raise subprocess.CalledProcessError(return_code, args, out, err)
