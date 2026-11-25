# language: es
@US05 @EP02
Característica: US05 Consultar las condiciones del plan
  Especificación propuesta para el piloto académico de PrismaReq.
  Los datos son sintéticos. El estado de ejecución se registra por AT en evidencias/ejecucion_actual/resultados.json.

  @AT09
  Escenario: Mostrar el límite registrado
    Dado que mi cuenta sintética tiene este plan:
      | nombre        | pantallas simultáneas |
      | Plan prueba A | 2                     |
    Cuando abro las condiciones de mi plan
    Entonces veo "Plan prueba A"
    Y veo un límite de "2" pantallas simultáneas

  @AT10
  Escenario: Informar un límite ausente
    Dado que el límite de mi plan sintético no está confirmado
    Cuando abro las condiciones de mi plan
    Entonces veo "Límite no disponible"
    Y no se utiliza el límite de otro plan ni un valor por defecto
