import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from Agenda.Agenda import Agenda

def test_agregar_contacto_nuevo():
    agenda = Agenda()
    agenda.agregar_contacto("Pedro", "1010")
    assert agenda.contactos["Pedro"] == "1010"

def test_agregar_contacto_existente_lanza_error():
    agenda = Agenda()
    agenda.agregar_contacto("Pedro", "1010")
    with pytest.raises(ValueError):
        agenda.agregar_contacto("Pedro", "9999")
