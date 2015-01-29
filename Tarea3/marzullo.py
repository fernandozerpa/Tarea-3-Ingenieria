'''
 marzullo.py
 @authors: Fernando Zerpa 05-39081
           Alejandra Preciado 07-41384
'''
import functools
import datetime

class Marzullo: 
    
    def formatoHoraValida(self, hora):
        try:
            datetime.datetime.strptime(hora, '%H:%M')
        except ValueError:
            raise ValueError("El formato de hora es incorrecto , el formato es 'hh:mm'")

    def horaValida(self, hora):
        
        if (datetime.datetime.strptime(hora, '%H:%M').hour < 6 or datetime.datetime.strptime(hora, '%H:%M').hour >18):
            raise Exception("Las Horas de reserva deben estarentre las 06:00 y las 18:00")  
        
    def algoritmo_Marzullo(self,intervalos):
        tabla = []
        hora= Marzullo()
        
        for ini,fin in intervalos:
            hora.horaValida(ini)
            hora.horaValida(fin)
            ini =datetime.datetime.strptime(ini, '%H:%M').hour
            fin =datetime.datetime.strptime(fin, '%H:%M').hour 
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
        beststart = datetime.time(beststart)
        bestend = datetime.time(bestend)
        '''beststart.strftime('%H:%M'), bestend.strftime('%H:%M')'''
        return ( best <= 10)
        