Feature: Registrar devoluciones en inventario

  Scenario: Cuando un envío cambia a estado "return", se debe registrar una devolución en InventoryService
    Given un envío existente con estado "pending"
    When se actualiza su estado a "return"
    Then se debe recibir un evento ShipmentReturned
    And se debe registrar una devolución en la tabla "product_returns"
