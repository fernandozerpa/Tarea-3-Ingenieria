'''
 pruebaMarzullo.py: Modulo de pruebas para el Algoritmo de reservas enun estacionamiento
 
 @authors: Fernando Zerpa 05-39081
           Alejandra Preciado 07-41384
'''

import unittest
from marzullo import Marzullo

class PruebaMarzullo(unittest.TestCase):

    '''Prueba Simple'''
    def testPruebaSimple(self):
        prueba = Marzullo()
        self.assertTrue(prueba.algoritmo_Marzullo((('08:00','12:00'),('11:00','13:00'),('10:00','12:00')))) 
        
    '''Prueba dos intervalos con la misma cantidad de puestos reservados'''
    def testDosIntervalosMismaCantidadDePuestos(self):
        prueba = Marzullo()
        self.assertTrue(prueba.algoritmo_Marzullo((('08:00','9:00'),('08:00','12:00'),('10:00','12:00')))) 
    
    '''Prueba para Offset iguales y tipe opuestos'''
    def testOffsetIgualesTypeOpuestos(self):
        prueba = Marzullo()
        self.assertTrue(prueba.algoritmo_Marzullo((('11:00','15:00'),('08:00','15:00'),('9:00','11:00'),('10:00','14:00'),('11:00','14:00'),('09:00','10:00'),('09:00','13:00'),('12:00','15:00'),('08:00','11:00'),('14:00','15:00'))))

    '''Caso en que se reserva el mismo puesto mas de 10 veces a la misma hora'''    
    def testMaximoDeReservasDeUnPuesto(self):
        n = []
        i=0
        while (i <11):
            n.append(('08:00','09:00'))
            i=i+1  
        prueba = Marzullo()
        self.assertFalse(prueba.algoritmo_Marzullo(n))
    
    '''Caso de llenar el estacionemiento'''    
    def testEstacionemientoLleno(self):
        n = []
        i=0
        while (i <9):
            n.append(('06:00','18:00'))
            i=i+1    
        prueba = Marzullo()
        self.assertTrue(prueba.algoritmo_Marzullo(n))
    
    '''Caso de agregar una reservacion con el estacionamiento lleno'''    
    def testAgregarUnoConEstacionamientoLleno(self):
        n = []
        i=0
        while (i <10):
            n.append(('06:00','18:00'))
            i=i+1
        n.append(('06:00','10:00'))    
        prueba = Marzullo()
        self.assertFalse(prueba.algoritmo_Marzullo(n))
            
if __name__ == "__main__":
    unittest.main()
