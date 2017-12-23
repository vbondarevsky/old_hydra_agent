from hydra_agent.config import Config
from hydra_agent.v8 import V8

config_ = Config()()
v8 = V8(config_)

__version__ = '0.0.1'
