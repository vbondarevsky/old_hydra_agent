from hydra_agent.config import Config
from hydra_agent.rac import Rac
from hydra_agent.ring import Ring
from hydra_agent.ring.license_manager import LicenseManager
from hydra_agent.v8 import V8

settings = Config()()
ring = Ring(settings)
license_manager = LicenseManager(settings)
rac = Rac(settings)

__version__ = '0.0.1'
