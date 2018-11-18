from hydra_agent.v8.connection_string import ConnectionString


class FileConnectionString(ConnectionString):

    def __init__(self, path, user=None, password=None, locale=None, version=None, page_size=None):
        assert not version or version in ["8.2.14", "8.3.8"]
        assert not page_size or page_size in [4096, 8192, 16384, 32768, 65536]

        self.path = path
        self.user = user
        self.password = password
        self.locale = locale
        self.version = version
        self.page_size = page_size

    def _get_properties(self):
        return {
            "path": "File",
            "user": "Usr",
            "password": "Pwd",
            "locale": "Locale",
            "version": "DBFormat",
            "page_size": "DBPageSize",
        }
