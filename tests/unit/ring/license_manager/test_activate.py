# This file is part of HYDRA - cross-platform remote administration
# system for 1C:Enterprise (https://github.com/vbondarevsky/hydra_agent).
# Copyright (C) 2017  Vladimir Bondarevskiy.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import subprocess

import pytest

from tests.unit import success_result, fail_result

info_1 = {'company': 'ООО "Рога и копыта"',  # минимум 5 символов. Этот или ФИО
          'last_name': 'Иванов',  # ФИО или компания
          'first_name': 'Иван',  # ФИО или компания
          'middle_name': 'Иванович',  # ФИО или компания
          'email': 'test@mail.ru',
          'country': 'Российская Федерация',  # обязательно
          'zip_code': '122000',  # обязательно
          'region': 'Москва',
          'district': '',
          'town': 'Москва',  # обязательно
          'street': 'Селезневская',  # обязательно
          'house': '9',  # не обязателен если заполнены building или apartment
          'building': '',  # не обязателен если заполнены house или apartment
          'apartment': ''}  # не обязателен если заполнены house или building

out_1 = 'Лицензия успешно получена.\n'
out_2 = 'Ошибка активации лицензии.\nПо причине: Ошибка ввода пинкода. Пинкод не укомплектован.\n'
out_3 = ('Ошибка активации лицензии.\nПо причине: Ошибка повторного получения лицензии. '
         'Параметры владельца лицензии отличаются от введенных ранее.\n')
out_4 = ('Ошибка получения списка лицензий.\nПо причине: Ошибка при работе с хранилищем лицензий.\n'
         ' По причине: Директория не найдена: "/var/lic".\n')


@pytest.mark.parametrize('out, license_info, serial, pin, previous_pin, path', [
    (out_1, info_1, '800123456', '123-123-123-123-123', None, '/var/1C/licenses'),
    (out_1, info_1, '800123456', '123-123-123-123-123', '222-123-123-123-123', None),
    (out_1, info_1, '800123456', '123-123-123-123-123', None, None),
], ids=['first_activation', 'second_activation', 'restore'])
def test_success(monkeypatch, fake_license_manager, out, license_info, serial, pin, previous_pin, path):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, out))
    assert fake_license_manager.activate(
        license_info=license_info,
        serial=serial,
        pin=pin,
        previous_pin=previous_pin,
        path=path)


@pytest.mark.parametrize('out, return_code, license_info, serial, pin, previous_pin, path', [
    (out_4, 1, info_1, '800123456', '123-123-123-123-123', None, None),
    (out_2, 1, info_1, '800123456', '123-123-123-123-123', None, None),
    (out_3, 1, info_1, '800123456', '123-123-123-123-123', None, None),
], ids=['wrong_pin', 'wrong_license_info', 'path'])
def test_fail(monkeypatch, fake_license_manager, return_code, out, license_info, serial, pin, previous_pin, path):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: fail_result(args, return_code, out))
    with pytest.raises(subprocess.CalledProcessError):
        fake_license_manager.activate(
            license_info=license_info,
            serial=serial,
            pin=pin,
            previous_pin=previous_pin,
            path=path)
