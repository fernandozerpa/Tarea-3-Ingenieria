'''
 marzullo.py
 @authors: Fernando Zerpa 05-39081
           Alejandra Preciado 07-41384
'''
import functools

class Marzullo: 

    def algoritmo_Marzullo(self,intervalos):
        tabla = []
    
        for ini,fin in intervalos:
            tabla.append((ini,-1))
            tabla.append((fin,+1))
     
        def comparar(x, y):
            comp = (x[0]>y[0]) - (x[0]<y[0])
            if comp == 0:
                comp = -((x[1]>y[1]) - (x[1]<y[1])) # regla para el mismo offset y type opuesto
            return comp
        tabla.sort(key = functools.cmp_to_key(comparar))
     
        best = 0
        cnt = 0
        for i in range(len(tabla) - 1):
            cnt = cnt - tabla[i][1]
            if best < cnt:
                best = cnt
                beststart = tabla[i][0]
                bestend   = tabla[i+1][0]
        return (beststart, bestend)