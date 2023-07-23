from twttr import shorten

def test_lowercase():
    assert shorten("my, name is atabek 6") == "my, nm s tbk 6"

def test_uppercase():
    assert shorten("MY, NAME IS ATABEK 6") == "MY, NM S TBK 6"