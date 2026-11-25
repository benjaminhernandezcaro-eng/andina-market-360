# Ficha Profesional - Andina Market 360

- Problema: Consolidar ventas multisede sin edicion manual.
- Flujo: data/ventas.csv -> src/resumen.py -> docs/data/resumen.json -> docs/index.html
- Decision 1: Usar solo biblioteca estandar Python (cero dependencias vulnerables).
- Decision 2: Desacoplar HTML estatico leyendo JSON generado automaticamente.
- Limitacion: Datos ficticios de 12 ventas didacticas.
