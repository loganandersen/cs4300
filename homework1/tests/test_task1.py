import task1

def test_hello_world(capsys) :
    task1.hello_world()
    output = capsys.readouterr().out
    assert output.strip() == "hello world"


