import pytest
from task3 import *

def test_sum_first_100_numbers() :
    "check if sum_first_100_numbers gets the first 100 numbers"
    # right side is the triangular number formula for 100
    # triangular numbers are the first n numbers added together
    assert (sum_first_100_numbers() == (100*100 + 100)/2) 

@pytest.mark.parametrize("num, expected", 
                         [(1,1),(-4,-1),
                         (-1,-1),
                         (100,1),
                         (0,0)])
def test_get_sign(num,expected) :
    "See if get sign works, compare with expected result"
    assert get_sign(num) == expected

def test_print_10_primes(capsys) : 
    first_10_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    print_10_primes()
    output = capsys.readouterr().out
    prime_str = '\n'.join(map(str,first_10_primes))
    assert output.strip() == prime_str 