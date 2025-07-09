Feature: Buscar contacto en la agenda

  Scenario: Usuario 1 busca un contacto existente
    Given una agenda con el contacto "Ana" y número "123"
    When busco el contacto "Ana"
    Then debería obtener el número "123"

  Scenario: Usuario 2 busca un contacto que no existe
    Given una agenda con el contacto "Pedro" y número "456"
    When busco el contacto "Lucas"
    Then no debería obtener ningún resultado
