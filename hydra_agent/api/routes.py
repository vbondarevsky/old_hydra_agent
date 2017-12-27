from hydra_agent.api.handler.license import LicenseHandler


def setup_routes(app):
    app.router.add_route('*', '/license', LicenseHandler)
