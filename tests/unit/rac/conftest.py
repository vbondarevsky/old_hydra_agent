import pytest

from hydra_agent import Rac, Config


@pytest.fixture
def fake_rac():
    settings = Config(source='rac:\n    path: /opt/1C/v8.3/x86_64')()
    return Rac(config=settings)
