import subprocess

import pytest

from tests.unit import success_result


def test_version(monkeypatch, fake_ring):
    monkeypatch.setattr(subprocess, 'run', lambda args, stdout, stderr: success_result(args, '0.8.0-1'))
    assert fake_ring.version == '0.8.0-1'


@pytest.mark.parametrize('out, expected', [
    (
            'Доступные модули:\n\n  license_manager@0.4.0:x86_64 - Утилита для работы с лицензиями.\n\n',
            [('license_manager', '0.4.0', 'x86_64', 'Утилита для работы с лицензиями.')]
    ),
    (
            'Доступные модули:\r\n  license_manager@0.3.0:x86_64 - Утилита для работы с лицензиями.\r\n',
            [('license_manager', '0.3.0', 'x86_64', 'Утилита для работы с лицензиями.')]
    ),
], ids=['linux_ru', 'windows_ru'])
def test_modules(monkeypatch, fake_ring, out, expected):
    monkeypatch.setattr(subprocess, 'run', lambda args, stdout, stderr: success_result(args, out))
    assert fake_ring.modules == expected
