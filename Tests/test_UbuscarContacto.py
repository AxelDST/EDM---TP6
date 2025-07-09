import pytest
from Agenda.Agenda import Agenda

@pytest.fixture
def agenda():
    ag = Agenda()
    ag.agregar_contacto("Ana", "123")
    ag.agregar_contacto("Pedro", "456")
    return ag

@pytest.mark.parametrize(
    "nombre, esperado",
    [
        ("Ana", "123"),
        ("Pedro", "456"),
        ("Lucas", None),             # contacto que no existe
        ("", None),                  # string vacío
        (None, None),                # búsqueda con None
        ("ANA", None),              # mayúsculas diferentes
        ("ana", None),              # minúsculas diferentes
    ]
)
def test_buscar_contacto_varios(agenda, nombre, esperado):
    assert agenda.buscar_contacto(nombre) == esperado
