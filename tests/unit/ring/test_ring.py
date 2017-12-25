import subprocess

import pytest

from tests.unit import success_result


def test_version(monkeypatch, fake_ring):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, '0.8.0-1'))
    assert fake_ring.version == '0.8.0-1'


@pytest.mark.parametrize('out, expected', [
    ('Доступные модули:\n\n\n', []),
    ('Доступные модули:\n\n  license_manager@0.4.0:x86_64 - Утилита для работы с лицензиями.\n\n',
     [('license_manager', '0.4.0', 'x86_64', 'Утилита для работы с лицензиями.')]),
], ids=['empty', 'license'])
def test_modules(monkeypatch, fake_ring, out, expected):
    monkeypatch.setattr(subprocess, 'run', lambda args, **kwargs: success_result(args, out))
    assert fake_ring.modules == expected
