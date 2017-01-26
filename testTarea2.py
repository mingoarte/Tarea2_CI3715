'''
Created on 26 ene. 2017

@author: ejsr
'''

import unittest
from datetime import *
import datetime

from Tarea2 import Tarifa, fecha_salida, fecha_entrada

class TarifaTester(unittest.TestCase):
    
    def testFechasValidas(self):
        self.assertTrue(not (fecha_salida < fecha_entrada), "La fecha de salida debe ser posterior a la de entrada.")
        
    def testRangoValidoD(self):
        self.assertTrue(not ((fecha_salida-fecha_entrada).seconds < 900), "Sevicio minimo es de 15 minutos")
        
    def testRangoValidoU(self):
        self.assertTrue(not ((fecha_salida-fecha_entrada).seconds > 432000), "Sevicio maximo es de cinco dias")
        

            