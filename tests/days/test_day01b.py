import pytest
from days import day01b

def test_look_string_for_numbers_works():
    testString = "twoa1b3c4"
    assert day01b.lookForStringNumbers(testString) == "t2oa1b3c4"

def test_look_string_for_all_numbers_works():
    testString = "onetwothreefourfivesixseveneightnine"
    assert day01b.lookForStringNumbers(testString) == "o1et2ot3ef4rf5es6xs7ne8tn9e"

def test_look_string_for_numbers_sharing_letters_works():
    testString = "eightwo"
    assert day01b.lookForStringNumbers(testString) == "e8t2o"

def test_look_string_without_numbers_works():
    testString = "abcdefghijklmnopqrstuvwxyz"
    assert day01b.lookForStringNumbers(testString) == "abcdefghijklmnopqrstuvwxyz"