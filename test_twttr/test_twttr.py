from twttr import shorten

def test_lowercase():
    shorten("my name is atabek") == "my nm s tbk"

def test_uppercase():
    shorten("MY NAME IS ATABEK") == "MY NM S TBK"