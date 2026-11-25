# language: es
@US03 @EP01
Característica: US03 Recuperarse de una búsqueda sin coincidencias
  Especificación propuesta para el piloto académico de PrismaReq.
  Los datos son sintéticos. El estado de ejecución se registra por AT en evidencias/ejecucion_actual/resultados.json.

  Antecedentes:
    Dado que el catálogo disponible contiene únicamente estos títulos:
      | id  | tema    | enfoque    |
      | D01 | océanos | científico |
      | D02 | océanos | narrativo  |

  @AT05
  Escenario: Informar que no existen coincidencias
    Cuando busco el tema "océanos" con enfoque "histórico"
    Entonces veo "No encontramos coincidencias"
    Y puedo modificar los filtros
    Y no se presentan títulos ajenos al filtro como coincidencias

  @AT06
  Escenario: Retirar un filtro
    Dado que estoy sin coincidencias para "océanos" e "histórico"
    Cuando retiro el filtro de enfoque
    Entonces los resultados contienen "D01" y "D02"
    Y se conserva el filtro de tema "océanos"
