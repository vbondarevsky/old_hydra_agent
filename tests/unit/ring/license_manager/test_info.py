import subprocess

import pytest

from tests.unit import success_result, fail_result


def test_info_success(monkeypatch, fake_license_manager):
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
    assert fake_license_manager.info(name='111111111111111-1111111111') == info


def test_info_fail(monkeypatch, fake_license_manager):
    def mock_result(args, stdout, stderr):
        return fail_result(
            args,
            1,
            'Проверка лицензии завершилась с ошибкой. Лицензия не найдена\n')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    with pytest.raises(Exception):
        fake_license_manager.info(name='111111111111111-1111111111')


def test_info_fail_path(monkeypatch, fake_license_manager):
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
        fake_license_manager.info(name='111111111111111-1111111111', path='/var/lic')
