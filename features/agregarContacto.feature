Feature: Agregar contacto a la agenda

  Scenario: Agregar un nuevo contacto correctamente
    Given una agenda vacía
    When agrego el contacto "Pedro" con el teléfono "1010"
    Then el contacto "Pedro" debe estar registrado con el teléfono "1010"

  Scenario: Intentar agregar un contacto existente
    Given una agenda con el contacto "Pedro" y teléfono "1010"
    When intento agregar el contacto "Pedro" con el teléfono "9999"
    Then debe lanzarse un error indicando que el contacto ya existe
