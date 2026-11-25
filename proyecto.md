# Proyecto Andina Market 360

Problema: Consolidar las ventas de Lima, Ica y Arequipa sin editar reportes manualmente.
Usuarios: Analista comercial, equipo de revision y coordinacion del curso.
Resultado esperado: Resumen automatico por sede, pruebas aprobadas y tablero web estatico.
Restriccion: Trabajar unicamente con datos ficticios y sin credenciales en archivos.

Preguntas de negocio:
1. Que sede lidera las ventas acumuladas?
2. Que producto y categoria presentan mayor rotacion?
3. Como cambia el total mensual segun nuevas transacciones?

## Herramientas
- Git: conserva el historial local de versiones y ramas del proyecto.
- GitHub: aloja el repositorio remoto y facilita Pull Requests e Issues.
- Python 3: ejecuta src/resumen.py y las pruebas en tests/test_resumen.py.

Flujo: archivo local -> Git local -> repositorio remoto -> revision del equipo
Nota: Ningun paso depende de que GitHub ejecute el script de ventas para versionar.

## Estructura de carpetas
andina-market-360/
├── data/ventas.csv
├── src/resumen.py
├── tests/test_resumen.py
├── docs/index.html, style.css, data/resumen.json
└── .github/workflows/ci.yml

Justificacion: docs/data/resumen.json es generado por Python para evitar edicion manual del CSV en la web.

## Criterios de exito
| Indicador | Meta | Responsable | Evidencia |
|---|---|---|---|
| Registros cargados | 12 operaciones CSV | Analista | python src/resumen.py |
| Totales por sede | Lima 814, Ica 555, Arequipa 476 | Script Python | docs/data/resumen.json |
| Pruebas automaticas | 4/4 pruebas OK | Revisor | python -m unittest discover -s tests -v |
| Tablero web | Visualizacion local sin errores | Web | http://localhost:8000 |
