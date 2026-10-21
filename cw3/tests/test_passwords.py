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

@pytest.mark.parametrize("password", [
    pytest.param(password_of_length(10)),
    pytest.param("#@AZÓŁ23"),
])
@pytest.mark.xfail(reason="DEF-HS-001")
# TODO: test_ep_valid – klasy poprawne (HS-3, HS-4)
def test_ep_valid(password):
    assert validate_password(password) is True


@pytest.mark.parametrize("password",[
    pytest.param(23234),
    pytest.param(["ads"]),
    pytest.param(True),
])
# TODO: test_ep_invalid – każda klasa niepoprawna osobno
def test_ep_invalid(password):
    with pytest.raises(TypeError):
        validate_password(password)


# TODO: test_bva_length_2p, test_bva_length_3p_extra
#       (użyj funkcji password_of_length)

@pytest.mark.parametrize("password",[
    pytest.param(password_of_length(8)),
    pytest.param(password_of_length(20)),
])
def test_bva_length_2p(password):
    assert validate_password(password) is True

@pytest.mark.parametrize("password",[
    pytest.param(password_of_length(7)),
    pytest.param(password_of_length(21)),
])
def test_bva_length_2p_negative(password):
    assert validate_password(password) is False
