# Issue #2: bug: cifra incorrecta tras editar CSV

- Datos de entrada: Muestra ficticia en data/ventas.csv (12 operaciones, total 1845.00).
- Pasos para reproducir:
  1. Editar data/ventas.csv sin regenerar docs/data/resumen.json.
  2. Abrir docs/index.html en http://localhost:8000.
- Resultado observado: El JSON mantiene cifras anteriores.
- Resultado esperado: Ejecutar python src/resumen.py --json docs/data/resumen.json tras editar CSV.
