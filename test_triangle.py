import sys
import pytest
import triangle

max_val = sys.maxsize


@pytest.mark.parametrize("x, y, z", ((1, 1, 1), (max_val, max_val, max_val)))
def test_equilateral(x, y, z):
    assert triangle.check_triangle(x, y, z) == "Equilateral Triangle"


@pytest.mark.parametrize("x, y, z", ((2, 1, 2), (max_val, max_val, max_val-10)))
def test_isosceles(x, y, z):
    assert triangle.check_triangle(x, y, z) == "Isosceles Triangle"


@pytest.mark.parametrize("x, y, z", ((2, 3, 4), (max_val - 10, max_val - 5, max_val)))
def test_scalene(x, y, z):
    assert triangle.check_triangle(x, y, z) == "Scalene Triangle"


@pytest.mark.parametrize("x, y, z", ((-1, -2, -3), (0, 2, 2), (4, 7, 16), (4.5, 5, 5.5), (max_val * 2, max_val, max_val), (None, 2, 2), ("a", "b", 43), ("%", "&", "=")))
def test_invalid(x, y, z):
    assert triangle.check_triangle(x, y, z) == "Error! Invalid data. Not a triangle."
