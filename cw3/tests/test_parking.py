"""Testy czarnoskrzynkowe: parking_fee (PK-1 ... PK-5)."""
import pytest

from sut import parking_fee


# EP – klasy poprawne (także klasy WYJŚĆ: 0 zł, 5 zł, 10 zł ...)
@pytest.mark.parametrize("minutes, fee", [
    pytest.param(600, 20.0, id="daily"),
    # TODO: pozostałe klasy poprawne
])
def test_ep_valid_classes(minutes, fee):
    assert parking_fee(minutes) == fee


# TODO: test_ep_out_of_range (ValueError), test_ep_wrong_type


# TODO: test_bva_2p, test_bva_3p_extra
