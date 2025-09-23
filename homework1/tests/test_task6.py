from task6 import *

def test_word_count() :
    """Tests if the word count of the file task6_read_me.txt is 104 (104 came from wc -w)"""
    assert word_count() == 104
