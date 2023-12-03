import pytest
from days import day03a

def test_look_for_first_number_beginning_correct():
    testmatrix = ["123...123"]
    [foundNumberStartColumn,foundNumberEndColumn] = day03a.lookForNumber(testmatrix,0,0)
    assert [foundNumberStartColumn,foundNumberEndColumn] == [0,2]

def test_look_for_first_number_middle_correct():
    testmatrix = ["...123.2."]
    [foundNumberStartColumn,foundNumberEndColumn] = day03a.lookForNumber(testmatrix,0,0)
    assert [foundNumberStartColumn,foundNumberEndColumn] == [3,5]

def test_look_for_first_number_end_correct():
    testmatrix = ["......123"]
    [foundNumberStartColumn,foundNumberEndColumn] = day03a.lookForNumber(testmatrix,0,0)
    assert [foundNumberStartColumn,foundNumberEndColumn] == [6,8]

def test_look_for_only_one_number_correct():
    testmatrix = ["......1.."]
    [foundNumberStartColumn,foundNumberEndColumn] = day03a.lookForNumber(testmatrix,0,0)
    assert [foundNumberStartColumn,foundNumberEndColumn] == [6,6]

def test_look_for_second_number_correct():
    testmatrix = ["123...123"]
    [foundNumberStartColumn,foundNumberEndColumn] = day03a.lookForNumber(testmatrix,0,3)
    assert [foundNumberStartColumn,foundNumberEndColumn] == [6,8]

def test_look_for_number_without_numbers_correct():
    testmatrix = ["........."]
    [foundNumberStartColumn,foundNumberEndColumn] = day03a.lookForNumber(testmatrix,0,0)
    assert [foundNumberStartColumn,foundNumberEndColumn] == [-1,-1]

def test_look_for_second_number_without_numbers_correct():
    testmatrix = ["123......"]
    [foundNumberStartColumn,foundNumberEndColumn] = day03a.lookForNumber(testmatrix,0,3)
    assert [foundNumberStartColumn,foundNumberEndColumn] == [-1,-1]

def test_adjacent_simbols_first_row_first_column():
    testmatrix = ["123...","...#.."]
    result = day03a.adjacentToASimbol(testmatrix,0,0,2)
    assert result == True

def test_adjacent_simbols_second_row_first_column():
    testmatrix = ["......","123...","...#.."]
    result = day03a.adjacentToASimbol(testmatrix,1,0,2)
    assert result == True

def test_adjacent_simbols_last_row_first_column():
    testmatrix = ["......","...#..","123..."]
    result = day03a.adjacentToASimbol(testmatrix,2,0,2)
    assert result == True

def test_adjacent_simbols_first_row_middle_column():
    testmatrix = ["...123...","......#.."]
    result = day03a.adjacentToASimbol(testmatrix,0,3,5)
    assert result == True

def test_adjacent_simbols_first_row_last_column():
    testmatrix = ["......123",".....@..."]
    result = day03a.adjacentToASimbol(testmatrix,0,6,8)
    assert result == True