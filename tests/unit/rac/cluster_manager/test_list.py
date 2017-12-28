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

from hydra_agent.rac.cluster_manager.cluster import Cluster
from tests.unit import success_result

out_1 = ('cluster                       : 73a6a1b2-db40-11e7-049e-000d3a2c0d8b\n'
         'host                          : 1C\n'
         'port                          : 1541\n'
         'name                          : "Локальный кластер"\n'
         'expiration-timeout            : 0\n'
         'lifetime-limit                : 0\n'
         'max-memory-size               : 0\n'
         'max-memory-time-limit         : 0\n'
         'security-level                : 0\n'
         'session-fault-tolerance-level : 0\n'
         'load-balancing-mode           : performance\n'
         'errors-count-threshold        : 0\n'
         'kill-problem-processes        : 0\n\n')
out_2 = ('cluster                       : 73a6a1b2-1111-11e7-049e-000d3a2c0d8b\n'
         'host                          : 1C\n'
         'port                          : 1541\n'
         'name                          : "Локальный кластер"\n'
         'expiration-timeout            : 0\n'
         'lifetime-limit                : 0\n'
         'max-memory-size               : 0\n'
         'max-memory-time-limit         : 0\n'
         'security-level                : 2\n'
         'session-fault-tolerance-level : 0\n'
         'load-balancing-mode           : memory\n'
         'errors-count-threshold        : 0\n'
         'kill-problem-processes        : 1\n\n')


@pytest.mark.parametrize('out, expected', [
    ('\n\n', []),
    (out_1, [Cluster(out_1)]),
    (out_1 + out_2, [Cluster(out_1), Cluster(out_2)])
], ids=['empty', 'one', 'few'])
def test_success(monkeypatch, fake_cluster_manager, out, expected):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, out))
    assert fake_cluster_manager.list() == expected

# TODO: Какие фейлы можно протестировать?
