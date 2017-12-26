import pytest

from hydra_agent import Config, LicenseManager


@pytest.fixture
def fake_license_manager():
    settings = Config(source='ring:\n  path: /opt/1C/1CE/x86_64/ring\n  java: /usr/lib/jvm/java-8-oracle')()
    return LicenseManager(config=settings)
