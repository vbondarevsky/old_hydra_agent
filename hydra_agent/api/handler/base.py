class BaseHandler:
    @property
    def base(self):
        return "/api"

    def build_route(self, path):
        return self.base + path
