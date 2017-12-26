from hydra_agent.rac.cluster_manager.cluster import Cluster

raw = ('cluster                       : 73a6a1b2-db40-11e7-049e-000d3a2c0d8b\n'
       'host                          : 1C\n'
       'port                          : 1541\n'
       'name                          : "Локальный кластер"\n'
       'expiration-timeout            : 20\n'
       'lifetime-limit                : 100\n'
       'max-memory-size               : 2500000\n'
       'max-memory-time-limit         : 300\n'
       'security-level                : 2\n'
       'session-fault-tolerance-level : 3\n'
       'load-balancing-mode           : performance\n'
       'errors-count-threshold        : 5\n'
       'kill-problem-processes        : 1\n\n')


def test_create_from_string():
    cluster = Cluster(raw=raw)
    assert cluster.host == '1C'
    assert cluster.port == 1541
    assert cluster.name == '"Локальный кластер"'
    assert cluster.expiration_timeout == 20
    assert cluster.lifetime_limit == 100
    assert cluster.max_memory_size == 2500000
    assert cluster.max_memory_time_limit == 300
    assert cluster.security_level == 2
    assert cluster.session_fault_tolerance_level == 3
    assert cluster.load_balancing_mode == 'performance'
    assert cluster.errors_count_threshold == 5
    assert cluster.kill_problem_processes == 1
