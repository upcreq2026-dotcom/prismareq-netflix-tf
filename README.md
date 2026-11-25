# PrismaReq para Netflix

Prototipo académico mínimo viable de exploración documental y consulta transparente de suscripción. No es un producto de Netflix. Versión 1.0.1-mvp.

## Abrir la demostración

En la carpeta descargada, abrir `docs/index.html` con Chrome, Edge o Firefox. No se requiere una cuenta Netflix, servidor ni pagos. Para ejecutar pruebas usar HTTP local, como hace el script de validación.

También puede publicarse en GitHub Pages desde `main` y `/docs`. La guía está en `GUIA_GITHUB.md`.

## Probar los recorridos

1. Elegir intereses → Océanos y Científico → Aplicar filtros → D01 → Ver ficha.
2. Océanos e Histórico → Sin coincidencias → Retirar filtro de enfoque.
3. Mi suscripción → cambiar cuenta de prueba entre C01, C02, C03 y C04.
4. Preferencias → Guardar con confirmación → Eliminar con confirmación.
5. Mi balance → consultar vistos y pendientes → vaciar pendientes de prueba.

## Contenido

- `docs/`: aplicación estática sin dependencias externas.
- `features/`: 11 archivos Gherkin, 22 códigos AT y 25 variantes al expandir Examples.
- `tests/`: 9 pruebas unitarias y comprobaciones de interfaz por identificador AT.
- `evidencias/`: registros reales de la ejecución técnica local; no entrevistas nuevas.
- `wireframes/`: dos SVG para importar en Figma.
- `diagramas/`: personas, empatía, As-Is, To-Be e Impact Map editables o exportados.
- `documentacion/`: alcance, trazabilidad, validación y decisiones.
- `colaboracion/`: fichas para que cada integrante registre una revisión real con su cuenta.

## Reproducir pruebas

Requiere Node.js y Python 3.12 o compatible. Desde la raíz:

```sh
node --test tests/model.test.cjs
python -m pip install -r requirements-tests.txt
python -m playwright install chromium
python tests/validar_mvp.py
```

El script inicia su propio servidor HTTP local. En GitHub Actions el flujo instala los navegadores y conserva un artefacto llamado `resultados-prismareq`. Un flujo verde significa que no fallaron las comprobaciones automatizadas; AT18 sigue requiriendo lector de pantalla real.

## Límites de los resultados

Los títulos D01–D05 y las cuentas C01–C04 son sintéticos. AT18 tiene cobertura estructural parcial. Las metas M1–M3 requieren personas y no se reportan como alcanzadas. El p95 describe estas interacciones locales con datos pequeños, no el rendimiento de Netflix ni de una red pública. La optimización evita reemplazar resultados idénticos; no se afirma una mejora estadística con dos series.

Las publicaciones, enlaces reales y contribuciones de GitHub se obtienen después de subir el paquete. No se incluye un historial de autores ficticios.
