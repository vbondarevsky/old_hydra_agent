from .base_config import BaseConfig


class RacConfig(BaseConfig):
    def __init__(self, path, host, port):
        self.path = path
        self.host = host
        self.port = port

    def __str__(self):
        return f"path={self.path}, host={self.host}, port={self.port}"
