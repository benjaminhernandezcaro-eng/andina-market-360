# Reto 1.1 - Nueva pregunta comercial
Pregunta: Cual es el ticket promedio de venta por sede (Lima, Ica, Arequipa)?
Archivo que produce la respuesta: docs/data/resumen.json (generado por src/resumen.py)
Calculo verificable: total_por_sede / operaciones_por_sede -> Lima S/ 203.50, Ica S/ 138.75, Arequipa S/ 119.00.

# Reto 1.2 - Mapa de tres roles del proyecto
1. Analista de Datos: mantiene data/ventas.csv ficticio y valida cifras con src/resumen.py.
2. Desarrollador Python/Web: actualiza logica en src/ y tablero en docs/, ejecutando unittest.
3. Revisor de Calidad: inspecciona diff, comprueba que pasan los 4 tests y aprueba la integracion.

# Reto 1.3 - Clasificacion de cinco acciones cotidianas
| Accion | Entorno | Justificacion |
|---|---|---|
| 1. Guardar instantanea con git commit | Git local | Se registra en .git sin internet |
| 2. Abrir un Pull Request para revision | Plataforma GitHub | Flujo web de colaboracion |
| 3. Editar un archivo .md o .py | Herramienta externa (editor) | Modificacion en disco local |
| 4. Crear una rama con git switch -c | Git local | Operacion local de historial |
| 5. Gestionar tareas en GitHub Issues | Plataforma GitHub | Seguimiento remoto del equipo |
