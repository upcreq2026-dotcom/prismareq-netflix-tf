# language: es
@US06 @EP02
Característica: US06 Consultar el precio y acceder a la gestión
  Especificación propuesta para el piloto académico de PrismaReq.
  Los datos son sintéticos. El estado de ejecución se registra por AT en evidencias/ejecucion_actual/resultados.json.

  @AT11
  Escenario: Mostrar el precio de la cuenta
    Dado que mi cuenta sintética tiene este registro vigente:
      | plan          | monto | moneda |
      | Plan prueba A | 29.90 | PEN    |
    Cuando abro el resumen de mi suscripción
    Entonces veo un monto de "29.90" y moneda "PEN"
    Y el registro se identifica como dato de prueba

  @AT12
  Escenario: Abrir la gestión sin modificar la suscripción
    Dado que estoy en el resumen de mi suscripción sintética activa
    Cuando selecciono "Gestionar suscripción"
    Entonces accedo a la pantalla de gestión
    Y mi plan, precio y estado permanecen sin cambios
