from hello import say_hello, add


def test_say_hello():
    # updated name for myself
    result = say_hello("Eric")
    assert "Eric Ortega" in result
    assert "IDS 706" in result


def test_add():
    #  math check
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
