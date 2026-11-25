import unittest
import os
import sys

# Agregar src al path para importar
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from resumen import cargar_ventas, calcular_resumen

class TestResumenVentas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ruta_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "ventas.csv"))
        cls.operaciones = cargar_ventas(ruta_csv)
        cls.resumen = calcular_resumen(cls.operaciones)

    def test_total_general(self):
        """Verificar que el gran total de ventas coincida exactamente con S/ 1845.00"""
        self.assertEqual(self.resumen["total_general"], 1845.00)

    def test_cantidad_operaciones(self):
        """Verificar que existan exactamente 12 operaciones ficticias"""
        self.assertEqual(self.resumen["total_operaciones"], 12)

    def test_sedes_presentes(self):
        """Verificar que esten presentes las tres sedes: Lima, Ica, Arequipa"""
        sedes = set(self.resumen["totales_por_sede"].keys())
        self.assertEqual(sedes, {"Lima", "Ica", "Arequipa"})

    def test_totales_por_sede(self):
        """Verificar los subtotales esperados por cada sede segun el caso didactico"""
        totales = self.resumen["totales_por_sede"]
        self.assertEqual(totales["Lima"], 814.00)
        self.assertEqual(totales["Ica"], 555.00)
        self.assertEqual(totales["Arequipa"], 476.00)

if __name__ == "__main__":
    unittest.main()
