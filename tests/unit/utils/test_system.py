from hydra_agent.utils import is_linux, is_windows, is_mac


def test_system_detection():
    assert (is_windows() + is_linux() + is_mac()) == 1
