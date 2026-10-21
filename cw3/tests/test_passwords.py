"""Testy czarnoskrzynkowe: validate_password (HS-1 ... HS-4)."""
import pytest

from sut import validate_password


def password_of_length(n):
    """Hasło z liter i cyfr o długości n, np. 5 -> 'a1a1a'."""
    return ("a1" * n)[:n]


def test_example_valid_password():
    assert validate_password("haslo123") is True


def test_example_wrong_type():
    with pytest.raises(TypeError):
        validate_password(None)


# TODO: test_ep_valid – klasy poprawne (HS-3, HS-4)
# TODO: test_ep_invalid – każda klasa niepoprawna osobno
# TODO: test_bva_length_2p, test_bva_length_3p_extra
#       (użyj funkcji password_of_length)
