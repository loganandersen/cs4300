# Roman numerals in python
from roman import toRoman, fromRoman
import pytest
from task7 import *

# Integers and their corresponding roman numerals
test_data = [(7,"VII"), (4,"IV"), (2000,"MM"), (2025,"MMXXV")]

@pytest.mark.parametrize("x,numeral", test_data)
def test_toRoman(x,numeral):
    """See if toRoman in roman package works"""
    assert toRoman(x) == numeral 

@pytest.mark.parametrize("x,numeral", test_data)
def test_fromRoman(x,numeral) :
    """See if fromRoman in roman package works"""
    assert  fromRoman(numeral) == x

@pytest.mark.parametrize("num1, num2, result", 
  [("IV","VI","X"),
   ("III", "X", "XIII"),
   (2,3,""),
   ("IV", 3, ""),
   (2,"I",""),
   ("CCC","CC","D")])
def test_add_roman(num1,num2,result):
    """Add roman numerals together, compare them with expected result"""
    assert add_roman_numerals(num1,num2) == result
