from os.path import join


class Rac:
    def __init__(self, config):
        self.path = join(config['rac']['path'], 'rac')

# TODO: кроссплатформенное управление сервером
