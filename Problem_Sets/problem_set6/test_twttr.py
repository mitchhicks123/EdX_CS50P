import twttr

#test single word
def test_shorten_single_word():
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("toast") == "tst"
    assert twttr.shorten("punters") == "pntrs"

#test multiple words
def test_shorten_multiple_words():
    assert twttr.shorten("Test Mitchell is amazing!") == "Tst Mtchll s mzng!"

#test no words
def test_shorten_no_words():
    assert twttr.shorten("") == ""
