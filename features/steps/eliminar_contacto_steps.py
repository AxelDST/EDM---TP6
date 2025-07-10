import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from behave import given, when, then
from Agenda.Agenda import Agenda

@given('que existe un contacto llamado "{nombre}" con teléfono "{telefono}"')
def step_impl(context, nombre, telefono):
    context.agenda = Agenda()
    context.agenda.agregar_contacto(nombre, telefono)

@given('que la agenda está vacía')
def step_impl(context):
    context.agenda = Agenda()

@when('elimino el contacto llamado "{nombre}"')
def step_impl(context, nombre):
    context.agenda.eliminar_contacto(nombre)

@when('intento eliminar el contacto llamado "{nombre}"')
def step_impl(context, nombre):
    try:
        context.agenda.eliminar_contacto(nombre)
    except Exception as e:
        context.error = str(e)

@then('el contacto "{nombre}" no debe encontrarse en la agenda')
def step_impl(context, nombre):
    assert context.agenda.buscar_contacto(nombre) is None

@then('se debe mostrar un error indicando que el contacto no existe')
def step_impl(context):
    assert context.error == "El contacto no existe."