import os.path


class Ring:
    def __init__(self, config):
        self.path = os.path.join(config.ring.path, "ring")

    # TODO: управление лицензиями
