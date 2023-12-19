import pytest
from calculator import square

def main():
    test_calculator()

def test_calculator_positive():
    assert square(2) == 4
    assert square(3) == 9 

def test_calculator_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_calculator_zero(): 
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

if __name__ == "__main__":
    main()