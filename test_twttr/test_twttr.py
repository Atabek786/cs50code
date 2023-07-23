from twttr import shorten

def test_lowercase():
    shorten("atabek") == "tbk"

def test_uppercase():
    shorten("ATABEK") == "TBK"