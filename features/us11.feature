# language: es
@US11 @EP01
Característica: US11 Consultar el balance voluntario
  Especificación propuesta para el piloto académico de PrismaReq.
  Los datos son sintéticos. El estado de ejecución se registra por AT en evidencias/ejecucion_actual/resultados.json.

  @AT21
  Escenario: Separar títulos vistos y pendientes
    Dado que opté por consultar el balance con estos registros:
      | título | grupo     |
      | D01    | visto     |
      | D02    | pendiente |
    Cuando abro el balance de mi perfil
    Entonces "D01" aparece en "Vistos"
    Y "D02" aparece en "Pendientes elegidos"

  @AT22
  Escenario: Tratar una categoría vacía
    Dado que no tengo títulos pendientes elegidos
    Cuando abro el balance
    Entonces esa categoría presenta un estado vacío
    Y puedo regresar al catálogo
    Y no se añaden títulos pendientes sin mi elección
