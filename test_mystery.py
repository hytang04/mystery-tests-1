import pytest

from mystery import mystery


def test_01():
    acc = mystery()
    assert callable(acc)


def test_02():
    acc = mystery()
    assert acc() == 0


def test_03():
    acc = mystery()
    assert acc(5) == 5
    assert acc() == 5


def test_04():
    acc = mystery(10)
    assert acc() == 10
    assert acc(5) == 15
    assert acc(2) == 17


def test_05():
    acc = mystery(3)
    assert acc(2) == 5
    assert acc(-4) == 1
    assert acc() == 1


def test_06():
    first = mystery(10)
    second = mystery(10)

    assert first(5) == 15
    assert second() == 10
    assert second(2) == 12
    assert first() == 15


def test_07():
    acc = mystery()
    assert acc("4") == 8


def test_08():
    acc = mystery()
    assert acc("3") == -3


def test_09():
    acc = mystery(10)
    assert acc("8") == 26
    assert acc("5") == 21


def test_10():
    acc = mystery()
    assert acc("  6  ") == 12
    assert acc("007") == 5


def test_11():
    acc = mystery()
    assert acc("tree") == 4


def test_12():
    acc = mystery()
    assert acc("cat") == -3


def test_13():
    acc = mystery()
    assert acc("hello") == 5
    assert acc("python") == -1


def test_14():
    acc = mystery(10)
    assert acc("AEIOU") == 5
    assert acc("Rhythm") == 11


def test_15():
    acc = mystery()
    assert acc("") == 0
    assert acc("bcdf") == 4


def test_16():
    acc = mystery(5)

    with pytest.raises(TypeError):
        acc([1, 2, 3])

    assert acc() == 5


def test_17():
    acc = mystery(7)

    with pytest.raises(TypeError):
        acc({"value": 4})

    with pytest.raises(TypeError):
        acc(3.14)

    assert acc() == 7


def test_18():
    first = mystery()
    second = mystery(100)

    assert first("4") == 8
    assert first("cat") == 5

    assert second("tree") == 104
    assert second("3") == 101

    assert first() == 5
    assert second() == 101
