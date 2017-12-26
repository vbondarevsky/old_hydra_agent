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
out_2 = ('cluster                       : 73a6a1b2-db40-11e7-049e-000d3a2c0d8b\n'
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


@pytest.mark.parametrize('out, expected', [
    ('\n\n', []),
    (out_1, [Cluster(out_1)]),
    (out_1 + out_2, [Cluster(out_1), Cluster(out_2)])
], ids=['empty', 'one', 'few'])
def test_success(monkeypatch, fake_cluster_manager, out, expected):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, out))
    assert fake_cluster_manager.list() == expected

# TODO: Какие фейлы можно протестировать?
