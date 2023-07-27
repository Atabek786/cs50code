from project import value, convert, gauge
import pytest

def test_uppercase():
    assert value("      HELLO, I WANT TO TAKE 100 BUCKS") == 0
def test_lowercase():
    assert value("hello, i want to take 100 bucks") == 0
def test_hey_uppcase():
    assert value("HEY, I WANT TO TAKE 100 BUCKS") == 20
def test_hey_lwrcase():
    assert value("  hey, i want to take 100 bucks") == 20
def test_other():
    assert value("wassup, i want to take 100 bucks") == 100


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_correct_output():
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'