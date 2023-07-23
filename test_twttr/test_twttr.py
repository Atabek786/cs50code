from twttr import shorten

def test_lowercase():
    assert shorten("my name is atabek") == "my nm s tbk"

def test_uppercase():
    assert shorten("MY NAME IS ATABEK") == "MY NM S TBK"