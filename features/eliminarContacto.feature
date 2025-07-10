Feature: Eliminar contacto de la agenda

  Scenario: Eliminar un contacto existente
    Given que existe un contacto llamado "Laura" con teléfono "4444"
    When elimino el contacto llamado "Laura"
    Then el contacto "Laura" no debe encontrarse en la agenda

  Scenario: Eliminar un contacto que no existe
    Given una agenda vacía
    When intento eliminar el contacto llamado "Sofía"
    Then se debe mostrar un error indicando que el contacto no existe