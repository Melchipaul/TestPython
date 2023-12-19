from source import is_even, reverse_str

def test_should_reverse_string():
    assert reverse_str('hello') == 'olleh'

def test_should_return_empty_string_for_empty_string():
    assert reverse_str('') == ''

def test_should_be_even():
    assert is_even(2)

def test_should_be_odd():
    assert not is_even(3)