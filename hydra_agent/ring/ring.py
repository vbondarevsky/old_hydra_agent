import re
from os.path import join

from hydra_agent.utils.system import run_command


class Ring:
    def __init__(self, config):
        self.path = join(config['ring']['path'], 'ring')

    @property
    def version(self):
        return run_command([self.path, '--version'])

    @property
    def modules(self):
        result = run_command([self.path, 'help', 'modules'])
        p = re.compile(r'[@|:|-]')

        modules = []
        for i in result.split('\n\n')[1:]:
            r = tuple(map(str.strip, p.split(i)))
            modules.append(tuple(map(str.strip, p.split(i))))
        return modules
