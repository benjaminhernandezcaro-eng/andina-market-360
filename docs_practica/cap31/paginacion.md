# Planificacion de Paginacion y Limites de API

Flujo: Solicitud -> Respuesta + cabeceras (X-RateLimit-Remaining / Link) -> Siguientes paginas -> Consolidacion
- Error 403 (Rate limit): respetar Retry-After y detener reintentos automaticos.
- Error 404 (No encontrado): registrar recurso invalido y no reintentar.
- Timeout: maximo 3 reintentos con espera exponencial.
