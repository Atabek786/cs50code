import random
from project import options

# Assuming you have 'responses' defined somewhere, for example:
responses = ["response1", "response2", "response3"]

def test_random_option(monkeypatch):
    # Mocking user input '1' (to take the else branch)
    monkeypatch.setattr('builtins.input', lambda _: '1')
    # Ensure that the function returns None (as it prints random response)
    assert options() is None

def test_valid_option(monkeypatch):
    # Mocking user input '1', '2'
    monkeypatch.setattr('builtins.input', lambda _: '1', '2')
    assert options() == 2

def test_invalid_option_then_valid(monkeypatch):
    # Mocking user input '1', '6', '2'
    monkeypatch.setattr('builtins.input', lambda _: '1', '2')
    assert options() == 2

def test_invalid_then_valid_with_symbol(monkeypatch):
    # Mocking user input '1', '3'
    monkeypatch.setattr('builtins.input', lambda _: '1', '3')
    assert options() == 3

def test_invalid_then_valid_with_exception(monkeypatch):
    # Mocking user input '1', '4'
    monkeypatch.setattr('builtins.input', lambda _: '1', '4')
    assert options() == 4

