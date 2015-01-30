'''
 marzullo.py
 @authors: Fernando Zerpa 05-39081
           Alejandra Preciado 07-41384
'''
import functools
import datetime

class Marzullo: 
    
    
    '''Funcion que valida el formato de la hora'''
    def formatoHoraValida(self, hora):
        try:
            datetime.datetime.strptime(hora, '%H:%M')
        except ValueError:
            raise ValueError("El formato de hora es incorrecto , el formato es 'hh:mm'")

    '''Funcion que valida el rango de las horas y la granularidad de solo horas'''
    def horaValida(self, hora):
        
        if (datetime.datetime.strptime(hora, '%H:%M').hour < 6 or datetime.datetime.strptime(hora, '%H:%M').hour >18):
            raise ValueError("Las Horas de reserva deben estarentre las 06:00 y las 18:00")  
        if (datetime.datetime.strptime(hora, '%H:%M').minute != 0 ):
            raise ValueError("Las Horas deben ser exactas, los minutos deben ser igual a cero, por ejemplo: 09:00")
        
    '''Algoritmo de Marzullo'''    
    def algoritmo_Marzullo(self,intervalos):
        tabla = []
        hora= Marzullo()
        
        for ini,fin in intervalos:
            hora.formatoHoraValida(ini)
            hora.formatoHoraValida(fin)
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
        return ( best <= 10)
        
