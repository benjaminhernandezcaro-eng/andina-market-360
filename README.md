# Andina Market 360

Caso practico del Cuaderno de Git y GitHub (36 capitulos).

## Objetivo
Consolidar ventas ficticias de Lima, Ica y Arequipa en un resumen JSON y un tablero web estatico sin datos reales.

## Requisitos y Datos
- Python 3 estándar (sin dependencias externas)
- Git
- Fuente de datos ficticios: [data/ventas.csv](data/ventas.csv)
- Manual detallado: [Manual](docs/manual.md) | [Guia de contribucion](CONTRIBUTING.md)

## Tabla de Indicadores (Ejemplo generado por Python)
| Sede | Indicador | Formula | Fuente |
|---|---|---|---|
| Lima | Total ventas | Suma(total) | data/ventas.csv |
| Ica | Total ventas | Suma(total) | data/ventas.csv |
| Arequipa | Total ventas | Suma(total) | data/ventas.csv |

*Nota: Los valores reales se calculan automaticamente; no deben tomarse como cifras reales de negocio.*

## Inicio rapido
```bash
python -m unittest discover -s tests -v
python src/resumen.py --json docs/data/resumen.json
python -m http.server 8000 --directory docs
```
