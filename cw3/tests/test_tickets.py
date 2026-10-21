"""Testy czarnoskrzynkowe: ticket_price (BL-1 ... BL-4)."""
import pytest

from sut import ticket_price


# EP – klasy poprawne: jedna typowa wartość z każdej klasy WEJŚCIA
# (uwaga: cena 10.0 dotyczy dwóch różnych grup wieku)
@pytest.mark.parametrize("age, price", [
    pytest.param(40, 20.0, id="normal"),
    # TODO: pozostałe klasy poprawne (bezpłatny, ulgowy x2)
])
def test_ep_valid_classes(age, price):
    assert ticket_price(age) == price


# TODO: test_ep_out_of_range (ValueError), test_ep_wrong_type (TypeError)


# TODO: test_bva_2p, test_bva_2p_out_of_domain, test_bva_3p_extra
#       (brzegi WSZYSTKICH klas – także skrajne brzegi dziedziny)
