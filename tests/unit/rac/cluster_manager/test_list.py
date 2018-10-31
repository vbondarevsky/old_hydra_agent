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

out_1 = ("cluster                       : aa8b5a4b-7c20-4982-a865-4a8bb8affcb1\n"
         "host                          : localhost\n"
         "port                          : 2541\n"
         "name                          : \"second\"\n"
         "expiration-timeout            : 0\n"
         "lifetime-limit                : 1345\n"
         "max-memory-size               : 0\n"
         "max-memory-time-limit         : 0\n"
         "security-level                : 0\n"
         "session-fault-tolerance-level : 3\n"
         "load-balancing-mode           : memory\n"
         "errors-count-threshold        : 0\n"
         "kill-problem-processes        : 0\n"
         "\n")

out_2 = ("cluster                       : aef2b782-b27d-428f-bba2-cf807d769f57\n"
         "host                          : localhost\n"
         "port                          : 1541\n"
         "name                          : \"name\"\n"
         "expiration-timeout            : 0\n"
         "lifetime-limit                : 0\n"
         "max-memory-size               : 0\n"
         "max-memory-time-limit         : 0\n"
         "security-level                : 0\n"
         "session-fault-tolerance-level : 0\n"
         "load-balancing-mode           : performance\n"
         "errors-count-threshold        : 0\n"
         "kill-problem-processes        : 0\n"
         "\n")

params1 = {
    "cluster": "aa8b5a4b-7c20-4982-a865-4a8bb8affcb1",
    "host": "localhost",
    "port": "2541",
    "name": "\"second\"",
    "expiration-timeout": "0",
    "lifetime-limit": "1345",
    "max-memory-size": "0",
    "max-memory-time-limit": "0",
    "security-level": "0",
    "session-fault-tolerance-level": "3",
    "load-balancing-mode": "memory",
    "errors-count-threshold": "0",
    "kill-problem-processes": "0",
}
params2 = {
    "cluster": "aef2b782-b27d-428f-bba2-cf807d769f57",
    "host": "localhost",
    "port": "1541",
    "name": "\"name\"",
    "expiration-timeout": "0",
    "lifetime-limit": "0",
    "max-memory-size": "0",
    "max-memory-time-limit": "0",
    "security-level": "0",
    "session-fault-tolerance-level": "0",
    "load-balancing-mode": "performance",
    "errors-count-threshold": "0",
    "kill-problem-processes": "0",
}
cluster1 = Cluster.from_dict(params1)
cluster2 = Cluster.from_dict(params2)


@pytest.mark.parametrize(
    "out, expected",
    [
        ("\n", []),
        (out_1, [cluster1]),
        (out_1 + out_2, [cluster1, cluster2]),
    ],
    ids=["empty", "one", "few"]
)
def test_success(monkeypatch, cluster_manager, out, expected):
    monkeypatch.setattr(subprocess, "run", lambda args, **kwargs: success_result(args, out))
    assert list(cluster_manager.list()) == expected

# TODO: Какие фейлы можно протестировать?
