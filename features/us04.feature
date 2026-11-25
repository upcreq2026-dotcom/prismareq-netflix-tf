# language: es
@US04 @EP03
Característica: US04 Preservar la elección sin pasos obligatorios
  Especificación propuesta para el piloto académico de PrismaReq.
  Los datos son sintéticos. El estado de ejecución se registra por AT en evidencias/ejecucion_actual/resultados.json.

  @AT07
  Escenario: Mantener el recorrido de referencia
    Dado el recorrido de prueba "Catálogo > Ficha del título"
    Y que no tengo preferencias guardadas
    Cuando abro un título sin activar el selector de intereses
    Entonces accedo a la ficha mediante el mismo recorrido
    Y no aparece una pantalla obligatoria adicional

  @AT08
  Escenario: Cerrar el selector sin confirmar
    Dado que no tengo filtros activos ni preferencias guardadas
    Y que seleccioné "océanos" en un selector aún sin confirmar
    Cuando cierro el selector
    Entonces regreso al catálogo sin aplicar esa selección
    Y no se guarda una preferencia en mi perfil
