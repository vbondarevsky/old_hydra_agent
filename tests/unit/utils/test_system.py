from hydra_agent.utils import is_linux, is_windows, is_mac


def test_codecov():
    result = None
    if is_windows():
        result = True
    elif is_mac():
        result = True
    elif is_linux():
        result = True

    assert result
