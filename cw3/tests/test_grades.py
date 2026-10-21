"""Testy czarnoskrzynkowe: grade_from_percent (OC-1 ... OC-4)."""
import pytest

from sut import grade_from_percent


# EP – klasy poprawne: jedna typowa wartość z każdej klasy
@pytest.mark.parametrize("percent, grade", [
    pytest.param(25, 2.0, id="fail"),
    pytest.param(55, 3.0, id="satisfactory"),
    pytest.param(65, 3.5, id="satisfactory plus"),
    pytest.param(75, 4.0, id="good"),
    pytest.param(85, 4.5, id="good plus"),
    pytest.param(95, 5.0, id="very good"),
])
def test_ep_valid_classes(percent, grade):
    assert grade_from_percent(percent) == grade


# EP – klasy niepoprawne (wartość): jeden test = jedna klasa
@pytest.mark.parametrize("percent", [
    pytest.param(-10, id="negative"),
    pytest.param(110, id="above"),
])
def test_ep_out_of_range(percent):
    with pytest.raises(ValueError):
        grade_from_percent(percent)

@pytest.mark.parametrize("percent",  [
    pytest.param(3.5, id="float"),
    pytest.param("455", id="str digit"),
    pytest.param("", id="empty string"),
    pytest.param("PLL", id="letters"),
])
@pytest.mark.xfail( reason="DEF-01", strict=True)
# TODO: test_ep_wrong_type – argumenty innego typu niż int (OC-4)
def test_ep_wrong_type(percent):
    with pytest.raises(TypeError):
        grade_from_percent(percent)


@pytest.mark.parametrize("percent, grade", [
    pytest.param(0, 2.0),
    pytest.param(50, 2.0),
    pytest.param(51, 3.0),
    pytest.param(60, 3.0),
    pytest.param(61, 3.5),
    pytest.param(70, 3.5),
    pytest.param(71, 4.0),
    pytest.param(80, 4.0),
    pytest.param(81, 4.5),
    pytest.param(90, 4.5),
    pytest.param(91, 5.0),
    pytest.param(100, 5.0),
])
# TODO: test_bva_2p – wszystkie wartości AWB 2-punktowej
def test_bva_2p(percent, grade):
    assert grade_from_percent(percent) == grade

@pytest.mark.parametrize("percent", [
    pytest.param(-1), pytest.param(101),
])
def test_bva_2p_negative(percent):
    with pytest.raises(ValueError):
        grade_from_percent(percent)

# TODO: test_bva_3p_extra – wartości, które dokłada
#       wersja 3-punktowa (tych, które są już w 2p, nie powtarzaj)
