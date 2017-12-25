import subprocess

import pytest

from tests.unit import success_result, fail_result


def test_list_empty(monkeypatch, fake_license_manager):
    def mock_result(args, stdout, stderr):
        return success_result(args, '\n')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    assert fake_license_manager.list() == []


def test_list_one_license(monkeypatch, fake_license_manager):
    def mock_result(args, stdout, stderr):
        return success_result(args, '332588056123456-8100123456\n')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    assert fake_license_manager.list() == ['332588056123456-8100123456']


def test_list_two_license_linux(monkeypatch, fake_license_manager):
    def mock_result(args, stdout, stderr):
        return success_result(
            args,
            '332588056123456-8100123456\n173211456654321-800654321\n')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    assert fake_license_manager.list() == ['332588056123456-8100123456', '173211456654321-800654321']


def test_list_two_license_windows(monkeypatch, fake_license_manager):
    def mock_result(args, stdout, stderr):
        return success_result(
            args,
            '123456533312696-8100920111\r\n123456530097928-800489222\r\n')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    assert fake_license_manager.list() == ['123456533312696-8100920111', '123456530097928-800489222']


def test_list_fail(monkeypatch, fake_license_manager):
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
        fake_license_manager.list()
