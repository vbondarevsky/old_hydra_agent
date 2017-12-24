from hydra_agent.config import Config
from hydra_agent.ring import Ring
from hydra_agent.ring.license_manager import LicenseManager
from hydra_agent.v8 import V8

config_ = Config()()
v8 = V8(config_)
ring = Ring(config_)
license_manager = LicenseManager(config_)

__version__ = '0.0.1'
