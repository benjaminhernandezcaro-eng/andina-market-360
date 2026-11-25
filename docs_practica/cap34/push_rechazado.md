# Diagnostico de Push Rechazado (non-fast-forward)

- Mensaje tipico: `! [rejected] main -> main (fetch first)`
- Diagnostico: `git fetch origin` seguido de `git log --oneline HEAD..origin/main`
- Solucion correcta: integrar primero (`git pull --ff-only` o `git merge origin/main`) antes de hacer push.
- Regla: Nunca usar `git push --force` de forma automatica.
