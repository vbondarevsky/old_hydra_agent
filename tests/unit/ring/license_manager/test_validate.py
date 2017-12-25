import subprocess

import pytest

from tests.unit import success_result, fail_result


def test_validate_success(monkeypatch, fake_license_manager):
    def mock_result(args, stdout, stderr):
        return success_result(args, 'Проверка лицензии "111111111111111-1111111111" выполнена успешно.\n')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    assert fake_license_manager.validate(name='111111111111111-1111111111')


def test_validate_fail(monkeypatch, fake_license_manager):
    def mock_result(args, stdout, stderr):
        return fail_result(
            args,
            1,
            'Проверка лицензии завершилась с ошибкой. Лицензия не найдена\n')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    with pytest.raises(Exception):
        fake_license_manager.validate(name='111111111111111-1111111111')


def test_validate_fail_path(monkeypatch, fake_license_manager):
    def mock_result(args, stdout, stderr):
        return fail_result(
            args,
            1,
            '\n'.join(['Ошибка получения списка лицензий.',
                       'По причине: Ошибка при работе с хранилищем лицензий.',
                       ' По причине: Директория не найдена: "/var/lic".',
                       '']))

    monkeypatch.setattr(subprocess, 'run', mock_result)
    with pytest.raises(Exception):
        fake_license_manager.validate(name='111111111111111-1111111111', path='/var/lic')
