import pytest

from hydra_agent.config import Config


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        Config(path='etc/not_exists')()
