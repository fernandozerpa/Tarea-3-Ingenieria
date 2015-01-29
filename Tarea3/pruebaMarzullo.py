'''
 pruebaMarzullo.py
 @authors: Fernando Zerpa 05-39081
           Alejandra Preciado 07-41384
'''



import unittest
from marzullo import Marzullo

class PruebaMarzullo(unittest.TestCase):


    def testPrueba1(self):
        prueba = Marzullo()
        self.assertEqual(prueba.algoritmo_Marzullo((('08:00','12:00'),('11:00','13:00'),('10:00','12:00'))), ('11:00','12:00')) 
    
    def testPrueba2(self):
        prueba = Marzullo()
        self.assertEqual(prueba.algoritmo_Marzullo((('08:00','9:00'),('08:00','12:00'),('10:00','12:00'))), ('08:00','09:00')) 
    
    def testPrueba3(self):
        prueba = Marzullo()
        self.assertEqual(prueba.algoritmo_Marzullo((('08:00','12:00'),('09:00','10:00'),('11:00','13:00'),('10:00','12:00'))), ('11:00','12:00')) 
    
    def testPrueba4(self):
        prueba = Marzullo()
        self.assertEqual(prueba.algoritmo_Marzullo((('08:00','12:00'),('09:00','10:00'),('11:00','13:00'),('14:00','15:00'))), ('09:00','10:00')) 
    
    def testPrueba5(self):
        prueba = Marzullo()
        self.assertEqual(prueba.algoritmo_Marzullo((('11:00','15:00'),('08:00','15:00'),('9:00','11:00'),('10:00','14:00'),('11:00','14:00'),('09:00','10:00'),('09:00','13:00'),('12:00','15:00'),('08:00','11:00'),('14:00','15:00'))), ('12:00','13:00'))


if __name__ == "__main__":
    unittest.main()
