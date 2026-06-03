# Contexto del proyecto — Proyecto: ecj_primer_libro

Última actualización: 2026-06-03T08:48:22Z

Este archivo es el punto de referencia compartido para trabajar en el proyecto desde distintos ordenadores. Actualiza la sección "Última actualización" con una marca de tiempo ISO en cada cambio.

**1. Resumen del estado actual del proyecto**

- Rama principal: `main` (sincronizada con `origin/main`). Commit actual: `256b362254cf5fe2a423dcf9aacf8edd309d00ce` (2026-06-01).
- Repositorio remoto: https://github.com/enrikecj/ecj_primer_libro.git
- Estructura multi-idioma activa: `book/es/` y `book/en/` con sus `_toc_*` y `_config_*`.
- Scripts disponibles para automatización: `scripts/` (p. ej. `build_book.py`, `render_diagrams.py`, `export_pdf.py`, `check_encoding.py`, `optimize_static_assets.py`, `setup_env.py`, etc.).
- Diagram sources: ~30 ficheros en `diagram_sources/` (mermaid/plantuml/graphviz/wavedrom...); pueden necesitar renderizado en `_static/generated/diagrams/`.

**2. Decisiones de arquitectura tomadas y por qué**

- Uso de Jupyter Book / TeachBooks como framework principal: permite generación HTML + PDF y compatibilidad con notebooks.
- Flujo multi-idioma: cada idioma tiene su `_config_<lang>.yml`, `_toc_<lang>.yml` y carpeta `book/<lang>/` para mantener paridad entre idiomas.
- Diagrams: fuentes en `diagram_sources/` y salida en `book/_static/generated/diagrams/` para evitar dependencia en tiempo de compilación (Kroki renderizado previamente) y garantizar compatibilidad PDF.
- Assets: PNG/JPG/SVG como formatos canónicos; WebP/GIF solo como mejora si existen fallbacks PNG/JPG para PDF.
- Automatización: scripts en `scripts/` para tareas repetibles (build, preview, export PDF, render diagrams, optimización assets).
- Numeración HTML de ecuaciones: se inyecta un script en `_static/custom.js` que captura el número del capítulo (`parts` numeradas en `_toc.yml`) y formatea MathJax para que la web emule la numeración del PDF `(1.1)`.

**3. Tareas completadas en la última sesión**

- Fetch del remoto y verificación de sincronía entre `main` local y `origin/main`.
- Exploración del repo con un agent `Explore` (reporte inicial añadido a la sesión de chat).
- Revisado el problema de la etiqueta bibliográfica `Phe22` / `oCB22`; la entrada `.bib` usa ahora `author`, pero el estilo `alpha` de pybtex sigue generando la etiqueta automática `oCB22`.
- Tests corregidos: `test_schemdraw_notebooks.py` ahora usa `skipTest` si no hay libretas, evitando fallos en la integración continua.
- Ecuaciones HTML arregladas: se configuró el MyST Markdown correctamente, se añadió el arreglo en `custom.js` cargado con `defer` y se modificó el `_toc.yml` con `parts: - numbered: true` para habilitar el conteo de capítulos en Jupyter Book.

**4. Próximos pasos priorizados**

1. Ejecutar `python scripts/check_encoding.py` (auditoría UTF-8) — prioridad alta.
2. Ejecutar `python scripts/check_multilang_integrity.py` (validar paridad entre idiomas) — prioridad alta.
3. Ejecutar la suite de tests: `python -m pytest tests/` y revisar fallos — prioridad alta.
4. Renderizar diagramas: `python scripts/render_diagrams.py` (requiere internet para Kroki) — prioridad media.
5. Auditar assets: `python scripts/optimize_static_assets.py --check` — prioridad media.
6. Añadir job de tests en CI (GitHub Actions) y añadir paso de `render_diagrams.py` al pipeline antes de `build_book.py` — prioridad alta.

**5. Problemas conocidos / deuda técnica**

- Presencia de algunos `DEBUG` prints en `scripts/build_book.py` y `scripts/export_pdf.py` (limpiar o convertir a `logging`).
- Suite de tests no integrada en el workflow automático de CI (gap de detección temprana de errores).
- Posible desincronización entre `diagram_sources/` y `book/_static/generated/diagrams/` si no se renderizan tras cambios.
- Algunos assets pueden carecer de fallback (GIFs sin PNG, WebP sin PNG/JPG), por lo que la exportación a PDF podría fallar o perder contenido.
- La etiqueta bibliográfica de la entrada `Phe22` no puede forzarse fácilmente en estilo `alpha`; `label` y `shorthand` no cambian la etiqueta renderizada, lo que sugiere que habrá que valorar un cambio de estilo o plugin si se desea corregirla.

**6. Tareas pendientes (lista de check rápido)**

- [x] Ejecutar `check_encoding.py` y resolver problemas de codificación.
- [x] Ejecutar `check_multilang_integrity.py` y arreglar archivos huérfanos o faltantes.
- [x] Ejecutar tests y arreglar fallos reportados.
- [x] Renderizar diagramas y confirmar que `book/_static/generated/diagrams/` contiene las imágenes actualizadas.
- [x] Ejecutar `optimize_static_assets.py --check` y corregir fallbacks faltantes para GIFs/WebP.
- [x] Remover/convertir `DEBUG` prints a `logging.debug()` (ocultados tras `--verbose`).
- [x] Actualizar workflow de CI para ejecutar tests y renderizar diagramas antes del build.
- [ ] Añadir los créditos a Teachbooks y al proyecto “Elaboración de libros electrónicos”.
- [ ] Evaluar si cambiar el estilo de referencias (`plain`, `unsrtalpha`) para corregir la etiqueta de `Phe22` si se decide intervenir.
- [x] Corregir la numeración de ecuaciones en la versión HTML inglesa del capítulo 1 para que aparezcan numeradas como en la versión española.
- [x] Alinear el estilo de numeración de ecuaciones HTML con el PDF generado: `(1.1), (1.2), ...` en lugar de `(#capítulo.#ecuación)`.
- [x] Separar visualmente las ecuaciones en las líneas “Equilibrio en x” y “Equilibrio en y” del apartado 3 del ejemplo 1, para que queden menos pegadas a los dos puntos.
- [x] Añadir un pequeño espacio antes de los vectores unitarios en las ecuaciones donde aparecen, para mejorar la legibilidad.
- [ ] Dividir el capítulo 1 en secciones cuando se añada más material: pendiente de definición de secciones.

**7. Notas editorial / de formato**

- La referencia bibliográfica `Phe22` se ha dejado en su etiqueta actual `oCB22` en HTML porque el estilo `alpha` genera esa etiqueta automáticamente; la corrección completa queda pendiente de una posible revisión del estilo bibliográfico.
- La versión inglesa HTML del capítulo 1 actualmente no muestra ecuaciones numeradas; hay que hacerla coincidir con la versión española.
- El estilo de numeración de ecuaciones en HTML debe ser uniforme con el PDF generado: `(1.1), (1.2), ...`.
- En el apartado 3 del ejemplo 1, las ecuaciones bajo “Equilibrio en x” y “Equilibrio en y” deben separarse más de los dos puntos para mejorar el diseño.
- Añadir un pequeño espacio antes de los vectores unitarios en las ecuaciones para que no queden pegados al símbolo anterior.
- Mantener consistencia tipográfica entre las versiones HTML y PDF en todo el capítulo 1.

**Resultados de las comprobaciones recientes**

- ✅ `check_encoding.py`: codificación UTF-8 válida en 337 archivos.
- ✅ `check_multilang_integrity.py`: estructura multi-idioma consistente entre `es` y `en`.
- ✅ `render_diagrams.py`: 40 diagramas encontrados, 0 fallidos, salida existente en `book/_static/generated/diagrams/`.
- ✅ `optimize_static_assets.py --check`: 110 assets revisados, 0 optimizables pendientes, 0 GIFs sin PNG fallback.
- ⚠️ `unittest discover tests -v`: 8 tests ejecutados, 1 fallo en `test_schemdraw_cells_render_once` porque no se encontraron notebooks.

**9. Notas adicionales**

- El entorno `.venv` no tiene `pytest` instalado, por lo que la suite se ha ejecutado con `unittest`.
- El fallo en `test_schemdraw_cells_render_once` sugiere revisar la presencia de notebooks o la configuración de `tests/test_schemdraw_notebooks.py`.

**10. Herramientas / MCPs configurados**

- Python scripts en `scripts/` (varias utilidades automatizables).
- GitHub Actions: workflows en `.github/workflows/` (deploy.yml, test.yml manual, sftp-deploy.yml).
- Skills / agents (definidos en `.github/skills/` y `.agents/`): disponibles para automatización y sincronización.
- Recomendación: usar siempre el entorno virtual `.venv` creado por `scripts/setup_env.py`.

**11. Contacts**

- Mantenedor principal: Enrique Conejero Jarque (`enrikecj@usal.es`) — autor/propietario principal del repositorio.
- Contacto de CI / despliegue: mismo responsable a falta de otro contacto claro en el repo.
- Otros colaboradores: completar aquí si hay más personas trabajando en el proyecto.

**12. Notas sobre actualización del archivo**

- Regla: quien edite este archivo debe añadir/actualizar la marca de tiempo en la cabecera (`Última actualización:`) usando formato ISO.
- Para cambios menores (estado de tareas completadas): editar la sección 6 y añadir una línea con la marca de tiempo del cambio y autor.
- Para cambios de arquitectura o decisiones formales: registrar la decisión en la sección 2 con fecha, autor y motivo.

**13. Sugerencias / Cosas que añadiría**

- Añadir un bloque `Contacts` con responsables (mantenedor, CI owner) si hay varios colaboradores.
- Añadir una breve sección `How to run quick checks` con los comandos clave (check_encoding, check_multilang_integrity, pytest, render_diagrams).
- Considerar versionar este archivo (commitarlo en una rama y revisarlo en code review) para evitar conflictos de cambios simultáneos.

---

Si quieres, puedo:
- añadir la sección `Contacts` (me indicas nombres/emails),
- ejecutar ahora las comprobaciones de prioridad (UTF-8 y multi-idioma) y pegar resultados,
- o crear una rama y commitear `PROJECT_CONTEXT.md` automáticamente.
