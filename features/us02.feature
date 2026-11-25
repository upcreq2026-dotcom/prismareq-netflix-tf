# language: es
@US02 @EP01
Característica: US02 Consultar contexto verificable
  Especificación propuesta para el piloto académico de PrismaReq.
  Los datos son sintéticos. El estado de ejecución se registra por AT en evidencias/ejecucion_actual/resultados.json.

  @AT03
  Escenario: Consultar metadatos respaldados
    Dado el título sintético "D01" con estos metadatos confirmados:
      | campo       | valor                          |
      | tema        | océanos                        |
      | enfoque     | científico                     |
      | descripción | Estudio de ecosistemas marinos |
      | fuente      | ficha editorial de prueba D01  |
    Cuando abro la ficha del título "D01"
    Entonces veo el tema, el enfoque y la descripción del registro
    Y puedo identificar la fuente del contexto mostrado

  @AT04
  Escenario: Reconocer un enfoque no confirmado
    Dado el título sintético "D05" sin enfoque confirmado
    Cuando abro la ficha del título "D05"
    Entonces veo "Enfoque no disponible"
    Y no se asigna una etiqueta inferida al título
