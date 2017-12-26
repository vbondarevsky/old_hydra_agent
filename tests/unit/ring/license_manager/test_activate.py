import subprocess

import pytest

from tests.unit import success_result

info = {'company': 'ООО "Рога и копыта"',
        'last_name': 'Иванов',
        'first_name': 'Иван',
        'middle_name': 'Иванович',
        'email': 'test@mail.ru',
        'country': 'Российская Федерация',
        'zip_code': '122000',
        'region': 'Москва',
        'district': '',
        'town': 'Москва',
        'street': 'Селезневская',
        'house': '9',
        'building': '',
        'apartment': ''}

# TODO: Доделать тесты

# @pytest.mark.parametrize('out, license_info, serial, pin, previous_pin, path, validate', [
#     ('', info, '800123456', '123-123-123-123-123', '', None, False),
#     ('', info, '800123456', '123-123-123-123-123', '222-123-123-123-123', None, False),
#     ('', info, '800123456', '123-123-123-123-123', '', None, False),
# ], ids=['first_activation', 'second_activation', 'restore'])
# def test_success(monkeypatch, fake_license_manager, out, license_info, serial, pin, previous_pin, path, validate):
#     monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, out))
#     assert fake_license_manager.activate(
#         license_info=license_info,
#         serial=serial,
#         pin=pin,
#         previous_pin=previous_pin,
#         path=path,
#         validate=validate)

# @pytest.mark.parametrize('out, return_code, path', [
#     (('Ошибка получения списка лицензий.\nПо причине: Ошибка при работе с хранилищем лицензий.\n'
#       ' По причине: Директория не найдена: "/var/lic".\n'), 1, '/var/lic'),
#     ('Проверка лицензии завершилась с ошибкой. Лицензия не найдена\n', 1, None),
# ], ids=['name', 'path'])
# def test_fail(monkeypatch, fake_license_manager, return_code, out, info, serial, pin, previous_pin, path, validate):
#     monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: fail_result(args, return_code, out))
#     with pytest.raises(subprocess.CalledProcessError):
#         fake_license_manager.activate(
#             license_info=info,
#             serial=serial,
#             pin=pin,
#             previous_pin=previous_pin,
#             path=path,
#             validate=validate)
