import subprocess

from tests.unit import success_result


def test_version(monkeypatch, fake_rac):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, '8.3.11.2899\n'))
    assert fake_rac.version == '8.3.11.2899'
