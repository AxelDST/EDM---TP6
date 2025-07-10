import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Agenda.Agenda import Agenda
import pytest

def test_eliminar_contacto_existente():
    agenda = Agenda()
    agenda.agregar_contacto("Juan", "123456")
    agenda.eliminar_contacto("Juan")
    assert agenda.buscar_contacto("Juan") is None

def test_eliminar_contacto_inexistente():
    agenda = Agenda()
    with pytest.raises(ValueError, match="El contacto no existe."):
        agenda.eliminar_contacto("Pedro")