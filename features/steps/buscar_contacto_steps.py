from behave import given, when, then
from Agenda.Agenda import Agenda

@given('una agenda con el contacto "{nombre}" y número "{telefono}"')
def step_given_agenda_con_contacto(context, nombre, telefono):
    context.agenda = Agenda()
    context.agenda.agregar_contacto(nombre, telefono)

@when('busco el contacto "{nombre}"')
def step_when_busco_contacto(context, nombre):
    context.resultado = context.agenda.buscar_contacto(nombre)

@then('debería obtener el número "{telefono}"')
def step_then_contacto_encontrado(context, telefono):
    assert context.resultado == telefono

@then('no debería obtener ningún resultado')
def step_then_contacto_no_encontrado(context):
    assert context.resultado is None
