import subprocess

from hydra_agent import ring
from tests.unit import success_result


def test_version(monkeypatch):
    def mock_result(args, stdout, stderr):
        return success_result(args, '0.8.0-1')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    assert ring.version == '0.8.0-1'


def test_modules(monkeypatch):
    def mock_result(args, stdout, stderr):
        return success_result(
            args, 'Доступные модули:\n\n  license_manager@0.4.0:x86_64 - Утилита для работы с лицензиями.\n\n')

    monkeypatch.setattr(subprocess, 'run', mock_result)
    assert ring.modules == [('license_manager', '0.4.0', 'x86_64', 'Утилита для работы с лицензиями.')]
