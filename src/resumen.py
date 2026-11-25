#!/usr/bin/env python3
"""
Script de consolidacion de ventas para Andina Market 360.
Usa exclusivamente librerias estandar de Python.
"""
import csv
import json
import os
import sys
import argparse

def cargar_ventas(ruta_csv="data/ventas.csv"):
    if not os.path.exists(ruta_csv):
        # Intentar ruta relativa al script
        ruta_alt = os.path.join(os.path.dirname(__file__), "..", ruta_csv)
        if os.path.exists(ruta_alt):
            ruta_csv = ruta_alt
        else:
            raise FileNotFoundError(f"No se encontro el archivo de ventas en: {ruta_csv}")
    
    operaciones = []
    with open(ruta_csv, mode="r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            operaciones.append({
                "id_venta": fila["id_venta"],
                "fecha": fila["fecha"],
                "sede": fila["sede"],
                "categoria": fila["categoria"],
                "producto": fila["producto"],
                "precio_unitario": float(fila["precio_unitario"]),
                "cantidad": int(fila["cantidad"]),
                "total": float(fila["total"])
            })
    return operaciones

def calcular_resumen(operaciones):
    totales_sede = {}
    conteo_sede = {}
    total_general = 0.0

    for op in operaciones:
        sede = op["sede"]
        monto = op["total"]
        totales_sede[sede] = round(totales_sede.get(sede, 0.0) + monto, 2)
        conteo_sede[sede] = conteo_sede.get(sede, 0) + 1
        total_general = round(total_general + monto, 2)

    return {
        "empresa": "Andina Market 360",
        "tipo_datos": "Ficticios",
        "total_operaciones": len(operaciones),
        "total_general": total_general,
        "totales_por_sede": totales_sede,
        "operaciones_por_sede": conteo_sede
    }

def imprimir_resumen(resumen):
    print("==================================================")
    print(f" {resumen['empresa']} - RESUMEN DE VENTAS")
    print("==================================================")
    print(f"Total de operaciones: {resumen['total_operaciones']}")
    print(f"Total general ventas: S/ {resumen['total_general']:.2f}")
    print("--------------------------------------------------")
    print("Ventas por Sede:")
    for sede, total in sorted(resumen["totales_por_sede"].items()):
        ops = resumen["operaciones_por_sede"][sede]
        print(f" - {sede:<10}: S/ {total:>8.2f} ({ops} operaciones)")
    print("==================================================")

def main():
    parser = argparse.ArgumentParser(description="Procesar ventas de Andina Market 360")
    parser.add_argument("--csv", default="data/ventas.csv", help="Ruta al archivo CSV de ventas")
    parser.add_argument("--json", help="Ruta para exportar el resumen en formato JSON")
    args = parser.parse_args()

    try:
        operaciones = cargar_ventas(args.csv)
        resumen = calcular_resumen(operaciones)
        imprimir_resumen(resumen)

        if args.json:
            os.makedirs(os.path.dirname(os.path.abspath(args.json)), exist_ok=True)
            with open(args.json, "w", encoding="utf-8") as f:
                json.dump(resumen, f, indent=2, ensure_ascii=False)
            print(f"[OK] Archivo JSON generado exitosamente en: {args.json}")
    except Exception as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
