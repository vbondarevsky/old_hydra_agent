import os.path
from typing import Dict

from hydra_agent.utils.system import run_command


class Rac:
    def __init__(self, config: Dict):
        self.path = os.path.join(config['rac']['path'], 'rac')
        self.server = config['rac']['server']
        self.port = config['rac']['port']

    @property
    def version(self):
        return self._run_command([self.path, '--version'])

    def _run_command(self, args):
        return run_command(self.__add_server([self.path, '--version']))

    def __add_server(self, args):
        args.append(f"{self.server}:{self.port}")
        return args
