# test_hello.py

from hello import say_hello, add


def test_say_hello_contains_name_and_course():
    out = say_hello("Eric")
    assert "Eric Ortega" in out
    assert "IDS 706" in out


def test_add_basic_cases():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
