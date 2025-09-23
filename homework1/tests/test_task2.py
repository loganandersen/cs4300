from task2 import *

def test_float() :
    assert type(floats(3)) == float
    assert type(floats(2)/2) == float
    assert type(floats(6)*2) == float

def test_int() :
    assert type(ints(2)) == int
    assert type(ints(20)/2) == float
    assert type(string(2)*ints(2)) == str

def test_string() :
    assert type(string(10)) == str
    assert type(len(string(3))) == int
    assert type(string(2) + string(4)) == str

def test_bools() :
    for i in map(bools,range(20)):
        if i :
            assert i 
        else :
            assert not i

    

