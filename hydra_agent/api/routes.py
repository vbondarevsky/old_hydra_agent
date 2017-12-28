from hydra_agent.api.handler.heartbeat import HeartbeatHandler
from hydra_agent.api.handler.license import LicenseHandler


def build_route(route):
    return f'/hydra_agent/api/v1{route}'


def setup_routes(app):
    app.router.add_route('*', build_route('/license'), LicenseHandler)
    app.router.add_route('*', build_route('/heartbeat'), HeartbeatHandler)
