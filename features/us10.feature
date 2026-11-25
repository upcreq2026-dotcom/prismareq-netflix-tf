# language: es
@US10 @EP03
Característica: US10 Medir el tiempo de carga de los flujos
  Especificación propuesta para el piloto académico de PrismaReq.
  Los datos son sintéticos. El estado de ejecución se registra por AT en evidencias/ejecucion_actual/resultados.json.

  @AT19
  Escenario: Obtener una medición reproducible
    Dado un entorno funcional con catálogo y versión identificados
    Y el protocolo propuesto incluye estos parámetros:
      | parámetro        | valor                          |
      | rutas            | resultados y ficha             |
      | calentamiento    | 5 solicitudes por ruta         |
      | muestras medidas | 100 por ruta                   |
      | concurrencia     | 1                              |
      | percentil        | rango más próximo              |
      | inicio           | activar consulta o abrir ficha |
      | fin              | contenido visible y utilizable |
    Cuando ejecuto el protocolo y registro cada muestra
    Entonces el informe separa tiempos y errores de cada ruta
    Y informa el p95 con la muestra 95 ordenada de cada ruta
    Y documenta dispositivo, red, navegador y estado de caché

  @AT20
  Escenario: Contrastar la meta provisional después de ajustes
    Dado que para el MVP se adopta la meta técnica provisional de p95 menor o igual a 2 s
    Y existe una línea base registrada con el mismo protocolo
    Cuando repito la medición después de los ajustes
    Entonces el p95 de resultados y el de fichas no exceden 2 s
    Y se conservan los registros antes y después de los ajustes
