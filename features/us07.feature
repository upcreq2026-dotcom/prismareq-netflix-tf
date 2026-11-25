# language: es
@US07 @EP03
Característica: US07 Mantener la exactitud de los datos del plan
  Especificación propuesta para el piloto académico de PrismaReq.
  Los datos son sintéticos. El estado de ejecución se registra por AT en evidencias/ejecucion_actual/resultados.json.

  @AT13
  Esquema del escenario: Contrastar cada cuenta con su registro
    Dado que la cuenta "<cuenta>" tiene el plan "<plan>"
    Y su registro contiene "<monto>", "<moneda>" y "<límite>"
    Cuando consulto el resumen y las condiciones de esa cuenta
    Entonces los valores visibles coinciden con ese registro
    Y no se mezclan datos de otras cuentas

    Ejemplos:
      | cuenta | plan | monto | moneda | límite |
      | C01    | A    | 29.90 | PEN    | 2      |
      | C02    | B    | 45.90 | PEN    | 4      |
      | C03    | C    | 9.90  | USD    | 1      |

  @AT14
  Escenario: Mostrar explícitamente los datos no confirmados
    Dado que el monto de la cuenta sintética "C04" no está confirmado
    Cuando consulto su resumen después de haber consultado "C01"
    Entonces el monto se muestra como "No disponible"
    Y no se reutiliza el monto de la cuenta "C01"
