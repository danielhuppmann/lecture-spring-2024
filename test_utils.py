from utils import add


def test_add():
    assert add(1, 2) == 3
    assert add(5, 5) == 10
    assert add(100, 1) == 101
