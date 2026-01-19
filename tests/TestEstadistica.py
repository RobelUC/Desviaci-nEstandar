import unittest
from src.logica.Estadistica import Estadistica

class TestEstadistica(unittest.TestCase):
    
    def setUp(self):
        self.estadistica = Estadistica()

    def test_desviacion_lista_vacia(self):
        resultado = self.estadistica.calcular_desviacion_estandar([])
        self.assertEqual(resultado, 0.0)

    def test_desviacion_un_elemento(self):
        resultado = self.estadistica.calcular_desviacion_estandar([5])
        self.assertEqual(resultado, 0.0)

    def test_desviacion_dos_elementos(self):
        resultado = self.estadistica.calcular_desviacion_estandar([2, 4])
        self.assertEqual(resultado, 1.0)
    
    def test_desviacion_varios_elementos(self):
        resultado = self.estadistica.calcular_desviacion_estandar([1, 2, 3])
        self.assertAlmostEqual(resultado, 0.81649658, places=4)