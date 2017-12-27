import pytest

from hydra_agent import Config
from hydra_agent.rac.cluster_manager.cluster import Cluster
from hydra_agent.rac.infobase_manager import InfoBaseManager


@pytest.fixture
def fake_infobase_manager():
    settings = Config(source='rac:\n    path: /opt/1C/v8.3/x86_64')()
    return InfoBaseManager(config=settings, cluster=Cluster(id='73a6a1b2-db40-11e7-049e-000d3a2c0d8b'))
