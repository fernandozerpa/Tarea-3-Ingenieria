'''
 marzullo.py
 @authors: Fernando Zerpa 05-39081
           Alejandra Preciado 07-41384
'''

class Marzullo: 

    def algoritmo_Marzullo(self,intervalos):
        tabla = []
    
        for ini,fin in intervalos:
            tabla.append((ini,-1))
            tabla.append((fin,+1))
     
        def getKey(item):
            return item[0]
        tabla.sort(key = getKey)
     
        best = 0
        cnt = 0
        for i in range(len(tabla) - 1):
            cnt = cnt - tabla[i][1]
            if best < cnt:
                best = cnt
                beststart = tabla[i][0]
                bestend   = tabla[i+1][0]
        return (beststart, bestend)