# language: es
@US09 @EP03
Característica: US09 Acceder mediante teclado y lector de pantalla
  Especificación propuesta para el piloto académico de PrismaReq.
  Los datos son sintéticos. El estado de ejecución se registra por AT en evidencias/ejecucion_actual/resultados.json.

  @AT17
  Escenario: Completar un recorrido con teclado
    Dado el prototipo funcional abierto en un entorno documentado
    Cuando completo el siguiente recorrido usando solo el teclado:
      | paso                                       |
      | abrir el selector de intereses             |
      | elegir tema y enfoque                      |
      | aplicar filtros y abrir una ficha          |
      | regresar y abrir el resumen de suscripción |
    Entonces todos los controles necesarios se pueden activar
    Y el foco es visible y sigue un orden coherente
    Y no existen bloqueos que impidan salir de un control

  @AT18
  Escenario: Anunciar controles y ausencia de coincidencias
    Dado un lector de pantalla y navegador documentados
    Cuando recorro los campos del selector
    Y aplico una combinación sin títulos disponibles
    Entonces se anuncian los nombres y estados de los campos
    Y se anuncia "No encontramos coincidencias"
