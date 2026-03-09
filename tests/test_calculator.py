"""Unit tests for the calculator module."""

import pytest

from app.calculator import add, divide, multiply, power, subtract


class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5

    def test_add_negative_numbers(self):
        assert add(-2, -3) == -5

    def test_add_floats(self):
        assert add(1.5, 2.5) == 4.0

    def test_add_zero(self):
        assert add(5, 0) == 5


class TestSubtract:
    def test_subtract_positive_numbers(self):
        assert subtract(5, 3) == 2

    def test_subtract_resulting_negative(self):
        assert subtract(3, 5) == -2


class TestMultiply:
    def test_multiply_positive_numbers(self):
        assert multiply(3, 4) == 12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0

    def test_multiply_negative(self):
        assert multiply(-3, 4) == -12


class TestDivide:
    def test_divide_positive_numbers(self):
        assert divide(10, 2) == 5.0

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_floats(self):
        assert divide(7.5, 2.5) == 3.0


class TestPower:
    def test_power_positive(self):
        assert power(2, 3) == 8

    def test_power_zero_exponent(self):
        assert power(5, 0) == 1

    def test_power_negative_exponent(self):
        assert power(2, -1) == 0.5
