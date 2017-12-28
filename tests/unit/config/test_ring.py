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


import pytest

from hydra_agent.config import Config


@pytest.mark.parametrize('source, expected', [
    ('test:', {'path': ''}),
    ('ring:\n    path: /opt/1C/v8.3/x86_64', {'path': '/opt/1C/v8.3/x86_64'}),
    ('ring:\n    path: /opt/1C/v8.3/x86_64\n    java: /usr/lib/jvm/java-8-oracle',
     {'path': '/opt/1C/v8.3/x86_64', 'java': '/usr/lib/jvm/java-8-oracle'}),
    ('ring:\n    path: C:\\Program Files\\1C\\1CE\\ring\n    java: C:\\Program Files\\Java\\jre-9.0.1',
     {'path': r'C:\Program Files\1C\1CE\ring', 'java': r'C:\Program Files\Java\jre-9.0.1'}),
], ids=['empty', 'path', 'path_java', 'windows_path_java'])
def test_success(source, expected):
    settings = Config(source=source)()
    assert settings['ring'] == expected
