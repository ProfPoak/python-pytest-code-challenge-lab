from palindrome import longest_palindromic_substring
import pytest

@pytest.mark.parametrize("input, expected", [
    ("racecar", "racecar"),
    ("a", "a"),
    ("cbbd", "bb"),
])
def test_basic_cases(input, expected):
    result = longest_palindromic_substring(input)
    assert result == expected

@pytest.mark.parametrize("input, expected", [
    ("a" * 1001, "Character count cannot exceed 1000. Please try again."),
    ("", "String cannot be empty"),
])
def test_invalid_inputs(input, expected):
    result = longest_palindromic_substring(input)
    assert result == expected

def test_equal_palindrome():
    result = longest_palindromic_substring("babad")
    assert result in ["aba", "bab"]

def test_no_palindrome_longer_than_one():
    result = longest_palindromic_substring("abcd")
    assert result in ["a", "b", "c", "d"]
