import pytest
from days import day01a

def test_first_last_number_with_two_different_numbers():
    testString = "a2b3c4"
    assert day01a.firstLastNumber(testString) == 24

def test_first_last_number_with_only_one_numbers():
    testString = "a2bcc"
    assert day01a.firstLastNumber(testString) == 22

def test_first_last_number_raises_exception_with_no_numbers():
    with pytest.raises(ValueError) as excinfo:  
        testString = "abccdef"
        day01a.firstLastNumber(testString)
    assert str(excinfo.value) == "String does not contain any numbers"  