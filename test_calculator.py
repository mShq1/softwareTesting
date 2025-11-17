import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.parametrize("left, right, result", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (1.5, 2.5, 4.0),
])
def test_add_positive(calc, left, right, result):
    assert calc.add(left, right) == result


@pytest.mark.parametrize("num, denom, output", [
    (6, 2, 3.0),
    (10, 5, 2.0),
    (-8, 2, -4.0),
    (5, 2, 2.5),
])
def test_division_valid(calc, num, denom, output):
    assert calc.divide(num, denom) == output


def test_division_by_zero(calc):
    with pytest.raises(ValueError, match="делить на ноль нельзя"):
        calc.divide(10, 0)


@pytest.mark.parametrize("number, is_prime", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (25, False),
    (0, False),
    (1, False),
])
def test_prime_values(calc, number, is_prime):
    assert calc.is_prime_number(number) == is_prime


def test_prime_invalid_type(calc):
    with pytest.raises(TypeError, match="ожидается целое число"):
        calc.is_prime_number(3.5)
