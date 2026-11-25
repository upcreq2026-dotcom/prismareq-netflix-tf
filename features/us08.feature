# language: es
@US08 @EP03
Característica: US08 Controlar las preferencias guardadas
  Especificación propuesta para el piloto académico de PrismaReq.
  Los datos son sintéticos. El estado de ejecución se registra por AT en evidencias/ejecucion_actual/resultados.json.

  @AT15
  Esquema del escenario: Guardar solo con confirmación
    Dado que mi perfil no tiene preferencias guardadas
    Cuando selecciono "océanos" y "<acción>"
    Entonces la preferencia "<estado>" en la gestión de mi perfil

    Ejemplos:
      | acción             | estado     |
      | confirmo guardar   | aparece    |
      | cierro sin guardar | no aparece |

  @AT16
  Escenario: Eliminar una preferencia
    Dado que guardé voluntariamente la preferencia "océanos"
    Cuando confirmo eliminar esa preferencia
    Y inicio una nueva búsqueda sin filtros manuales
    Entonces la preferencia no aparece en la gestión del perfil
    Y la nueva búsqueda no aplica la preferencia eliminada
