import os.path


class Rac:
    def __init__(self, config):
        self.path = os.path.join(config.rac.path, "rac")

# TODO: кроссплатформенное управление сервером
