import pytest
from days import day03b

def test_look_for_first_number_beginning_correct():
    testmatrix = ["123...123"]
    [foundNumberStartColumn,foundNumberEndColumn] = day03b.lookForNumber(testmatrix,0,0)
    assert [foundNumberStartColumn,foundNumberEndColumn] == [0,2]

def test_look_for_first_number_middle_correct():
    testmatrix = ["...123.2."]
    [foundNumberStartColumn,foundNumberEndColumn] = day03b.lookForNumber(testmatrix,0,0)
    assert [foundNumberStartColumn,foundNumberEndColumn] == [3,5]

def test_look_for_first_number_end_correct():
    testmatrix = ["......123"]
    [foundNumberStartColumn,foundNumberEndColumn] = day03b.lookForNumber(testmatrix,0,0)
    assert [foundNumberStartColumn,foundNumberEndColumn] == [6,8]

def test_look_for_only_one_number_correct():
    testmatrix = ["......1.."]
    [foundNumberStartColumn,foundNumberEndColumn] = day03b.lookForNumber(testmatrix,0,0)
    assert [foundNumberStartColumn,foundNumberEndColumn] == [6,6]

def test_look_for_second_number_correct():
    testmatrix = ["123...123"]
    [foundNumberStartColumn,foundNumberEndColumn] = day03b.lookForNumber(testmatrix,0,3)
    assert [foundNumberStartColumn,foundNumberEndColumn] == [6,8]

def test_look_for_number_without_numbers_correct():
    testmatrix = ["........."]
    [foundNumberStartColumn,foundNumberEndColumn] = day03b.lookForNumber(testmatrix,0,0)
    assert [foundNumberStartColumn,foundNumberEndColumn] == [-1,-1]

def test_look_for_second_number_without_numbers_correct():
    testmatrix = ["123......"]
    [foundNumberStartColumn,foundNumberEndColumn] = day03b.lookForNumber(testmatrix,0,3)
    assert [foundNumberStartColumn,foundNumberEndColumn] == [-1,-1]

def test_one_adjacent_number():
    testmatrix = ["*.....","123......"]
    result, numbers = day03b.howManyAdjacentsNumbers(testmatrix,0,0)
    assert result == 1
    assert numbers[0] == 123

def test_two_adjacent_numbers_down():
    testmatrix = ["...*.....","123.456.."]
    result, numbers = day03b.howManyAdjacentsNumbers(testmatrix,0,3)
    assert result == 2
    assert numbers == [123,456]

def test_two_adjacent_numbers_inline():
    testmatrix = ["123*456..","........"]
    result, numbers = day03b.howManyAdjacentsNumbers(testmatrix,0,3)
    assert result == 2
    assert numbers == [123,456]

def test_four_adjacent_numbers_everywhere():
    testmatrix = ["...789...","123*456..","...654.."]
    result, numbers = day03b.howManyAdjacentsNumbers(testmatrix,1,3)
    assert result == 4
    assert numbers == [789,123,456,654]