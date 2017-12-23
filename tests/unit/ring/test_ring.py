import subprocess
from subprocess import run


def license_list():
    run(['ring', 'license', 'list'])


def test_license_list(monkeypatch):
    def mockreturn(monkeypatch):
        return '333388056484632-8100111160\n172211456905900-800111993\n'

    monkeypatch.setattr(subprocess, 'run', mockreturn)

    r = license_list()
    assert r == '333388056484632-8100111160\n172211456905900-800111993\n'
