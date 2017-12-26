import pytest

from hydra_agent import Config
from hydra_agent.rac.cluster_manager import ClusterManager


@pytest.fixture
def fake_cluster_manager():
    settings = Config(source='rac:\n    path: /opt/1C/v8.3/x86_64')()
    return ClusterManager(config=settings)
