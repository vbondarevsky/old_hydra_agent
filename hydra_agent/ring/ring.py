import os.path
from os.path import join
from subprocess import run


class Ring:
    def __init__(self, config):
        self.path = join(config['ring']['path'], "ring")

    # TODO: управление лицензиями

    @property
    def version(self):
        result = run(self.path, '--version')

    @property
    def modules(self):
        result = run([self.path, 'help', 'modules'])
