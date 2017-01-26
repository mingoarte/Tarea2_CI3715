'''
Tarea 2
Domingo Arteaga, 11-10058
Edgar Silva, 11-10968

'''

import unittest
from datetime import *
import datetime

from Tarea2 import *

class TarifaTester(unittest.TestCase):
    
    def setUp(self):
        self.tasa = Tarifa(tasa_dias_semana=1.0, tasa_fines_semana=2.0)
        self.precio = calcularPrecio(self.tasa, fecha_entrada, fecha_salida)
    
    def testFechasValidas(self):
        self.assertTrue(not (fecha_salida < fecha_entrada), "La fecha de salida debe ser posterior a la de entrada.")
        
    def testRangoValidoD(self):
        self.assertTrue(not ((fecha_salida-fecha_entrada).seconds < 900), "Sevicio minimo es de 15 minutos")
        
    def testRangoValidoU(self):
        self.assertTrue(not ((fecha_salida-fecha_entrada).seconds > 432000), "Sevicio maximo es de cinco dias")
        
    def testTasasValidas(self):
        self.assertTrue(not (precio_normal <= 0), "Las tasas deben ser positivas.")
        self.assertTrue(not (precio_fin_semana <= 0), "Las tasas deben ser positivas.")
        
    def testTasaFloat(self):
        self.assertTrue(not (type(precio_normal) is not float), "Las tasas deben ser decimales.")
        self.assertTrue(not (type(precio_fin_semana) is not float), "Las tasas deben ser decimales.")
        
    def testTasasDiferentes(self):
        self.assertTrue(not (precio_normal == precio_fin_semana), "Las tasa diaria debe ser diferente a la de los fines de semana.")
        
    #def testPrecioFloat(self):
    #    self.assertTrue(not (type(self.precio) is not float), "El precio a pagar debe ser decimal.")
