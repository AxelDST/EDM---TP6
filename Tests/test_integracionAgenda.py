import pytest
from Agenda.Agenda import Agenda

def test_flujo_completo_agenda():
    # Se crea la agenda
    agenda = Agenda()

    # Agregamos contactos
    contactos = [
        ("Ana", "123"),
        ("Pedro", "456"),
        ("Lucas", "789")
    ]
    for nombre, telefono in contactos:
        agenda.agregar_contacto(nombre, telefono)

    # Se verifica que se puedan buscar
    assert agenda.buscar_contacto("Ana") == "123"
    assert agenda.buscar_contacto("Pedro") == "456"

    # Se eliminar a uno
    agenda.eliminar_contacto("Pedro")

    # Se verificar que ya no está y los otros sí
    assert agenda.buscar_contacto("Pedro") is None
    assert agenda.buscar_contacto("Ana") == "123"
    assert agenda.buscar_contacto("Lucas") == "789"
