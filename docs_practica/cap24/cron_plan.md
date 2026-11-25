# Planificacion Periodica (cron)

- Expresion: `30 8 * * 1` (todos los lunes 08:30 UTC = 03:30 hora Lima).
- Control de duplicados: `concurrency: group: semanal-andina`.
- Justificacion: Frecuencia semanal evita consumo innecesario de minutos en Actions.
