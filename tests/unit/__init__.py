import subprocess


def success_result(args, out):
    return subprocess.CompletedProcess(args, 0, out.encode(), b'')


def fail_result(args, return_code, out):
    return subprocess.CompletedProcess(
        args, return_code, out.encode(), b'')
