import subprocess

import pytest

from tests.unit import success_result, fail_result

info = ('Информация о пользователе:\n'
        '    Имя: Иван\n'
        '    Отчество: Иванович\n'
        '    Фамилия: Иванов\n'
        '    e-mail: ivan@ivanov.ru\n'
        '    Компания: ООО "Рога и копыта"\n'
        '    Страна: Российская Федерация\n'
        '    Индекс: 300022\n'
        '    Регион/область: Тульская обл\n'
        '    Город: Тула г\n'
        '    Улица: Свободы ул\n'
        '    Дом: 99\n'
        'Информация о продукте:\n'
        '    Дата комплектации: 00:00:00 18.10.2017\n'
        '    Регистрационный номер: 800123456G0')


@pytest.mark.parametrize('out, expected', [
    (info, info),
], ids=['found'])
def test_success(monkeypatch, fake_license_manager, out, expected):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, out))
    assert fake_license_manager.info(name='111111111111111-1111111111') == expected


@pytest.mark.parametrize('out, return_code, path', [
    (('Ошибка получения списка лицензий.\nПо причине: Ошибка при работе с хранилищем лицензий.\n'
      ' По причине: Директория не найдена: "/var/lic".\n'), 1, '/var/lic'),
    ('Проверка лицензии завершилась с ошибкой. Лицензия не найдена\n', 1, None),
], ids=['name', 'path'])
def test_fail(monkeypatch, fake_license_manager, out, return_code, path):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: fail_result(args, return_code, out))
    with pytest.raises(subprocess.CalledProcessError):
        fake_license_manager.info(name='111111111111111-1111111111', path=path)
