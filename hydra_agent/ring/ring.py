import os
import os.path
import re
from typing import Dict

from hydra_agent.utils.system import run_command, is_windows


class Ring:
    def __init__(self, config: Dict):
        self.path = os.path.join(config['ring']['path'], 'ring' + '.cmd' if is_windows() else '')
        self.java = config['ring']['java']

    @property
    def version(self):
        return run_command([self.path, '--version'])

    @property
    def modules(self):
        result = run_command([self.path, 'help', 'modules'])
        p = re.compile(r'[@:-]')

        modules = []
        for i in result.split('\n')[1:]:
            if not i.strip():
                continue
            modules.append(tuple(map(str.strip, p.split(i))))
        return modules

    def _run_command(self, args):
        os.environ['JAVA_HOME'] = self.java
        return run_command(args)
