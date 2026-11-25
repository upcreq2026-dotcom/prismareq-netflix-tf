# language: es
@US01 @EP01
Característica: US01 Seleccionar intereses documentales
  Especificación propuesta para el piloto académico de PrismaReq.
  Los datos son sintéticos. El estado de ejecución se registra por AT en evidencias/ejecucion_actual/resultados.json.

  Antecedentes:
    Dado el siguiente catálogo sintético de prueba:
      | id  | tema    | enfoque    | disponible |
      | D01 | océanos | científico | sí         |
      | D02 | océanos | narrativo  | sí         |
      | D03 | espacio | científico | sí         |
      | D04 | océanos | científico | no         |

  @AT01
  Escenario: Combinar tema y enfoque
    Cuando selecciono el tema "océanos" y el enfoque "científico"
    Y aplico los filtros
    Entonces la lista de resultados contiene únicamente el título "D01"

  @AT02
  Escenario: Omitir la selección
    Dado que no tengo preferencias guardadas ni filtros activos
    Cuando selecciono "Explorar sin filtros"
    Entonces puedo abrir un título del catálogo disponible
    Y no se exige elegir un tema ni un enfoque
