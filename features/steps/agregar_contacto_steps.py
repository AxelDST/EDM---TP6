import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from behave import given, when, then
from Agenda.Agenda import Agenda

@given('una agenda vacía')
def step_impl(context):
    context.agenda = Agenda()

@given('una agenda con el contacto "{nombre}" y teléfono "{telefono}"')
def step_impl(context, nombre, telefono):
    context.agenda = Agenda()
    context.agenda.agregar_contacto(nombre, telefono)

@when('agrego el contacto "{nombre}" con el teléfono "{telefono}"')
def step_impl(context, nombre, telefono):
    context.agenda.agregar_contacto(nombre, telefono)

@when('intento agregar el contacto "{nombre}" con el teléfono "{telefono}"')
def step_impl(context, nombre, telefono):
    try:
        context.agenda.agregar_contacto(nombre, telefono)
    except Exception as e:
        context.exception = e

@then('el contacto "{nombre}" debe estar registrado con el teléfono "{telefono}"')
def step_impl(context, nombre, telefono):
    assert context.agenda.buscar_contacto(nombre) == telefono

@then('debe lanzarse un error indicando que el contacto ya existe')
def step_impl(context):
    assert hasattr(context, "exception")
    assert str(context.exception) == "El contacto ya existe."
