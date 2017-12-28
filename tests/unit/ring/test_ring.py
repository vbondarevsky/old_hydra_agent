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

from tests.unit import success_result


def test_version(monkeypatch, fake_ring):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, '0.8.0-1'))
    assert fake_ring.version == '0.8.0-1'


@pytest.mark.parametrize('out, expected', [
    ('Доступные модули:\n\n\n', []),
    ('Доступные модули:\n\n  license_manager@0.4.0:x86_64 - Утилита для работы с лицензиями.\n\n',
     [('license_manager', '0.4.0', 'x86_64', 'Утилита для работы с лицензиями.')]),
], ids=['empty', 'license'])
def test_modules(monkeypatch, fake_ring, out, expected):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, out))
    assert fake_ring.modules == expected
