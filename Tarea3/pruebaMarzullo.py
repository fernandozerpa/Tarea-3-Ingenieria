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
        self.assertEqual(prueba.algoritmo_Marzullo(((8,12),(11,13),(10,12))), (11,12)) 
    
    def testPrueba2(self):
        prueba = Marzullo()
        self.assertEqual(prueba.algoritmo_Marzullo(((8,9),(8,12),(10,12))), (8,9)) 
    
    def testPrueba3(self):
        prueba = Marzullo()
        self.assertEqual(prueba.algoritmo_Marzullo(((8,12),(9,10),(11,13),(10,12))), (11,12)) 
    
    def testPrueba4(self):
        prueba = Marzullo()
        self.assertEqual(prueba.algoritmo_Marzullo(((8,12),(9,10),(11,13),(14,15))), (9,10)) 
    
    def testPrueba5(self):
        prueba = Marzullo()
        self.assertEqual(prueba.algoritmo_Marzullo(((11,15),(8,15),(9,11),(10,14),(11,14),(9,10),(9,13),(12,15),(8,11),(14,15))), (12,13)) 


if __name__ == "__main__":
    unittest.main()
