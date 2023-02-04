from plates import is_valid

#test license plate length
def test_is_valid_length():
    assert is_valid("ttttttt") == False
    assert is_valid("t") == False
    assert is_valid("tttt") == True

#test to make sure the license plate starts with the proper characters
def test_is_valid_start_values():
    assert is_valid("aa") == True
    assert is_valid("a1") == False
    assert is_valid("12") == False

#test for valid punctuation
def test_is_valid_punctuation():
    assert is_valid("aa!") == False
    assert is_valid("aaa") == True

#test to make sure license plate uses proper numbers
def test_is_valid_number_0():
    assert is_valid("aa0") == False
    assert is_valid("aa1") == True
