import pytest
import math

"""Tested functions"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def pow(a, b):
    return a ** b


def float_div(a, b):
    try:
        return a / b
    except ValueError as e:
        print(e)


def int_div(a, b):
    try:
        return a // b
    except ValueError as e:
        print(e)


"""Tests"""

@pytest.mark.parametrize("a, b, expected", 
                         [(1, 2, 3),
                          (1, -3, -2),
                          (0, 0, 0)])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", 
                         [(1, 2, -1),
                          (1, -3, 4),
                          (0, 0, 0)])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", 
                         [(1, 2, 2),
                          (1, -3, -3),
                          (0, 4, 0),
                          (5, 0, 0)])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", 
                         [(1, 2, 0.5),
                          (2, 3, 0.67),
                          (4, 2, 2.0)])
def test_float_div(a, b, expected):
    assert pytest.approx(float_div(a, b), rel=0.01, abs=0.0000001) == expected


@pytest.mark.parametrize("func", [(float_div), (int_div)])
def test_division_by_zero(func):
    with pytest.raises(ZeroDivisionError) as err_info:
        func(1, 0)
    assert "division" in str(err_info.value)
    assert "by zero" in str(err_info.value)


@pytest.mark.parametrize("a, b, expected", 
                         [(1, 2, 0),
                          (2, 3, 0),
                          (4, 2, 2),])
def test_int_div(a, b, expected):
    assert int_div(a, b) == expected