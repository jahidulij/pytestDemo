import pytest

values = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75)
]


@pytest.mark.parametrize("num1, num2, value", values)
def test_multiplication(num1, num2, value):
    assert num1 * num2 == value
