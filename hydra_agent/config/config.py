from os.path import dirname, abspath, join

from yaml import load

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


class Config:
    def __init__(self, path=None, source=''):
        self.path = path or join(dirname(dirname(dirname(abspath(__file__)))), 'etc', 'hydra_agent.yml')
        self.source = source or None

    def __call__(self, *args, **kwargs):
        if self.source:
            return load(self.source, Loader=Loader)
        else:
            with open(self.path) as f:
                return load(f, Loader=Loader)
