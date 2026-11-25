def agrupar_ventas_por_sede(registros):
    """Agrupa montos de una lista de diccionarios {sede, total} en laboratorio."""
    acumulado = {}
    for item in registros:
        sede = item.get('sede', 'Desconocida')
        monto = float(item.get('total', 0.0))
        acumulado[sede] = round(acumulado.get(sede, 0.0) + monto, 2)
    return acumulado

if __name__ == '__main__':
    muestra = [
        {'sede': 'Lima', 'total': 100.0},
        {'sede': 'Lima', 'total': 50.5},
        {'sede': 'Ica', 'total': 80.0},
    ]
    res = agrupar_ventas_por_sede(muestra)
    assert res == {'Lima': 150.5, 'Ica': 80.0}, f'Error: {res}'
    print('Prueba laboratorio OK:', res)
