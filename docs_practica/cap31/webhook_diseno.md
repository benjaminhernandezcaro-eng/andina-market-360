# Diseno de Webhook Seguro (Documental)

- Evento: push
- URL receptora ficticia: https://ejemplo-local.invalid/webhook/andina (no recibe datos reales)
- Seguridad: verificar firma HMAC-SHA256 en cabecera X-Hub-Signature-256 usando secreto fuera del repo.
- Control: registrar X-GitHub-Delivery para evitar procesar duplicados.
