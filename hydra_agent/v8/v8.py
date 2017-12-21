import os.path


class V8:
    def __init__(self, config):
        self.path = os.path.join(config.v8.path, "1cv8")

    def create_ib(self, ib):
        pass
        # TODO: сделать создание ИБ

    def update_cf(self):
        pass
        # TODO: сделать обновление конфигурации

    def update_ib(self):
        pass
        # TODO: сделать обновление конфигурации ИБ
