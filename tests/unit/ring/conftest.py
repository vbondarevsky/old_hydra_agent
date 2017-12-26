import pytest

from hydra_agent import Ring, Config


@pytest.fixture
def fake_ring():
    settings = Config(source='ring:\n  path: /opt/1C/1CE/x86_64/ring\n  java: /usr/lib/jvm/java-8-oracle')()
    return Ring(config=settings)
