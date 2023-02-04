from bank import value


#test hello greeting
def test_value_with_hello():
    assert value("Hello") == 0
    assert value("hello") == 0

#test a h word greeting
def test_value_with_h():
    assert value("HI") == 20
    assert value("hey there") == 20
    assert value("Hola") == 20

#test a greeting with no h
def test_value_with_none():
    assert value("Bonjour") == 100
    assert value("excuse me") == 100
