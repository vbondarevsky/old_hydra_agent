import subprocess

import pytest

from hydra_agent import license_manager
from tests.unit import success_result, fail_result


def test_list_empty(monkeypatch):
    def mock_result(args, stdout, stderr):
        return success_result(args, '\n')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    assert license_manager.list() == []


def test_list_one_license(monkeypatch):
    def mock_result(args, stdout, stderr):
        return success_result(args, '332588056123456-8100123456\n')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    assert license_manager.list() == ['332588056123456-8100123456']


def test_list_two_license(monkeypatch):
    def mock_result(args, stdout, stderr):
        return success_result(args, '332588056123456-8100123456\n173211456654321-800654321\n')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    assert license_manager.list() == ['332588056123456-8100123456', '173211456654321-800654321']


def test_list_fail(monkeypatch):
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
        license_manager.list()


def test_validate_success(monkeypatch):
    def mock_result(args, stdout, stderr):
        return success_result(args, 'Проверка лицензии "111111111111111-1111111111" выполнена успешно.\n')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    assert license_manager.validate(name='111111111111111-1111111111')


def test_validate_fail(monkeypatch):
    def mock_result(args, stdout, stderr):
        return fail_result(
            args,
            1,
            'Проверка лицензии завершилась с ошибкой. Лицензия не найдена\n')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    with pytest.raises(Exception):
        license_manager.validate(name='111111111111111-1111111111')


def test_validate_fail_path(monkeypatch):
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
        license_manager.validate(name='111111111111111-1111111111', path='/var/lic')


def test_info_success(monkeypatch):
    info = '\n'.join(['Информация о пользователе:',
                      '    Имя: Иван',
                      '    Отчество: Иванович',
                      '    Фамилия: Иванов',
                      '    e-mail: ivan@ivanov.ru',
                      '    Компания: ООО "Рога и копыта"',
                      '    Страна: Российская Федерация',
                      '    Индекс: 300022',
                      '    Регион/область: Тульская обл',
                      '    Город: Тула г',
                      '    Улица: Свободы ул',
                      '    Дом: 99',
                      'Информация о продукте:',
                      '    Дата комплектации: 00:00:00 18.10.2017',
                      '    Регистрационный номер: 800123456G0'])

    def mock_result(args, stdout, stderr):
        return success_result(args, info)

    monkeypatch.setattr(subprocess, 'run', mock_result)
    assert license_manager.info(name='111111111111111-1111111111') == info


def test_info_fail(monkeypatch):
    def mock_result(args, stdout, stderr):
        return fail_result(
            args,
            1,
            'Проверка лицензии завершилась с ошибкой. Лицензия не найдена\n')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    with pytest.raises(Exception):
        license_manager.info(name='111111111111111-1111111111')


def test_info_fail_path(monkeypatch):
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
        license_manager.info(name='111111111111111-1111111111', path='/var/lic')
