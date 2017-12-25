import subprocess

import pytest

from tests.unit import success_result, fail_result


@pytest.mark.parametrize('out, expected', [
    ('\n', []),
    ('332588056123456-8100123456\n', ['332588056123456-8100123456']),
    ('332588056123456-8100123456\n173211456654321-800654321\n',
     ['332588056123456-8100123456', '173211456654321-800654321'])
], ids=['empty', 'one', 'few'])
def test_success(monkeypatch, fake_license_manager, out, expected):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, out))
    assert fake_license_manager.list() == expected


@pytest.mark.parametrize('out, return_code, path', [
    (('Ошибка получения списка лицензий.\nПо причине: Ошибка при работе с хранилищем лицензий.\n'
      ' По причине: Директория не найдена: "/var/lic".\n'), 1, '/var/lic'),
], ids=['wrong_path'])
def test_fail(monkeypatch, fake_license_manager, out, return_code, path):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: fail_result(args, return_code, out))
    with pytest.raises(subprocess.CalledProcessError):
        fake_license_manager.list(path=path)
