# Bitacora de Fallos y Correcciones

- Fecha: 24/11/2026
- Diagnostico: Asercion fallida en tests/test_resumen.py al simular total esperado incorrecto.
- Causa: Valor esperado alterado en rama de ensayo (999.00 vs 814.00).
- Correccion: Restitucion del valor calculado real desde data/ventas.csv.
- Prueba posterior: python -m unittest discover -s tests -v -> Ran 6 tests OK.
