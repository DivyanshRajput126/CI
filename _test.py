import pytest

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def fifth_power(x):
    return x ** 5

def test_square():
    assert square(2) == 4, "Test failed: square of 2 should be 4" 
    assert square(3) == 9, "Test failed: square of 3 should be 9"
    assert square(-1) == 1, "Test failed: square of -1 should be 1"
    assert square(0) == 0, "Test failed: square of 0 should be 0"

def test_cube():
    assert cube(2) == 8, "Test failed: cube of 2 should be 8"
    assert cube(3) == 27, "Test failed: cube of 3 should be 27"
    assert cube(-1) == -1, "Test failed: cube of -1 should be -1"
    assert cube(0) == 0, "Test failed: cube of 0 should be 0"

def test_fifth_power():
    assert fifth_power(2) == 32, "Test failed: fifth power of 2 should be 32"
    assert fifth_power(3) == 243, "Test failed: fifth power of 3 should be 243"
    assert fifth_power(-1) == -1, "Test failed: fifth power of -1 should be -1"
    assert fifth_power(0) == 0, "Test failed: fifth power of 0 should be 0"

def test_invalid_output():
    with pytest.raises(TypeError):
        square("string")