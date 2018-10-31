class BaseHandler:
    @property
    def base(self):
        return "/hydra_agent/api/v1"

    def build_route(self, path):
        return self.base + path
