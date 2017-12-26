import os.path
from typing import Dict

from hydra_agent.utils.system import run_command


class Rac:
    def __init__(self, config: Dict):
        self.path = os.path.join(config['rac']['path'], 'rac')

    @property
    def version(self):
        return run_command([self.path, '--version'])
