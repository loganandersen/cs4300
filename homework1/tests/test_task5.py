import pytest
from task5 import *

@pytest.mark.parametrize("name, number", 
                         [("Logan",100),
                          ("Mason",101),
                          ("Hamilton",103),
                          ("Linus",105),
                          ("Cade",104)])
def test_students(name,number) :
    "checks if the students dictionary key points to the right ID"
    assert students[name] == number

def test_print_first_3_books(capsys):
    "Checks if the first 3 books that I listed are correct"
    print_first_3_books()
    output = capsys.readouterr().out.strip()
    books_as_string = """Homer: Illiad
Dennis Ritchie: C programming language
Chris Hanson: Software design for flexibility"""
    assert output == books_as_string
