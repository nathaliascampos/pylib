
import pytest

from pylib import normalize_strings


@pytest.fixture
def string_snake():
    return 'Atenção \N{SNAKE}'

# @pytest.fixture
# def string_aeiou():
#     return 'áéíóú'


def test_remove_non_ascii(string_snake):

    # EXERCISE
    new_string = normalize_strings.remove_non_ascii(string_snake)

    # ASSERT
    assert new_string == 'ateno '


def test_non_ascii_normalized(string_snake):

    # EXERCISE
    new_string = normalize_strings.remove_non_ascii_normalized(string_snake)

    # ASSERT
    assert new_string == 'atencao FAILED'
