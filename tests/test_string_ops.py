"""Unit tests for the string_ops module."""

from app.string_ops import reverse_string, to_uppercase


class TestToUppercase:
    def test_lowercase_input(self):
        assert to_uppercase("hello") == "HELLO"

    def test_mixed_case_input(self):
        assert to_uppercase("Hello World") == "HELLO WORLD"

    def test_already_uppercase(self):
        assert to_uppercase("PYTHON") == "PYTHON"

    def test_empty_string(self):
        assert to_uppercase("") == ""

    def test_numbers_and_symbols(self):
        assert to_uppercase("abc123!") == "ABC123!"


class TestReverseString:
    def test_simple_string(self):
        assert reverse_string("hello") == "olleh"

    def test_palindrome(self):
        assert reverse_string("racecar") == "racecar"

    def test_empty_string(self):
        assert reverse_string("") == ""

    def test_single_character(self):
        assert reverse_string("x") == "x"

    def test_string_with_spaces(self):
        assert reverse_string("hello world") == "dlrow olleh"
