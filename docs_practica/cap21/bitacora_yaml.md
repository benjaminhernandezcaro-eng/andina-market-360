# Analisis Comentado de .github/workflows/ci.yml

| Clave YAML | Funcion |
|---|---|
| name | Nombre visible del flujo en Actions ('Pruebas') |
| on | Disparadores: push y pull_request hacia main |
| permissions | Permiso minimo de solo lectura (contents: read) |
| jobs.test | Ejecuta ubuntu-latest, checkout, setup-python 3.11 y unittest |
