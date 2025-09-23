import pytest
from task4 import *


@pytest.mark.parametrize("price, percent, result", 
                         [(100,10,90),(20.5,10.3,18.3885),
                         (0.2,100,0),
                         (20,4,19.2),
                         (30.4,3.0,29.488)])
def test_calculate_discount(price,percent,result) :
    assert calculate_discount(price,percent) == result  