# Permisos de Integracion (Solo Lectura de Issues)

- Operacion necesaria: GET /repos/{owner}/{repo}/issues
- Permiso minimo: issues: read (se eliminan permisos de escritura y admin).
- Diseno: GitHub App con permisos granulares es preferible a token personal amplio.
- Seguridad: Ninguna clave guardada en el repositorio.
