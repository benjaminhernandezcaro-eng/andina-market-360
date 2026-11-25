# Guia de Autenticacion SSH Segura

- Comando local: `ssh-keygen -t ed25519 -C "practica@example.com"`
- Archivo publico (`id_ed25519.pub`): el unico que se agrega en GitHub -> Settings -> SSH keys.
- Archivo privado (`id_ed25519`): permanece exclusivamente en ~/.ssh con passphrase.
- Verificacion oficial: `ssh -T git@github.com` (sin publicar huellas ni claves).
