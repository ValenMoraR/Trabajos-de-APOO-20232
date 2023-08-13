#2 # Cree una clase Punto que represente un punto en el plano cartesiano.

#3 # A la clase del punto anterior, defínale los siguientes métodos:
# - Un método mostrar que imprima por consola las coordenadas del punto
# - Un método mover que cambie las coordenadas del punto
# - Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.

import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show_point(self):
        print(f"Coordenadas del punto 1: ({self.x}, {self.y})")
        
    def distance(self, a_point):
        dx= self.x - a_point.x
        dy= self.y - a_point.y
        distance= math.sqrt(dx**2 + dy**2)
        print(f"La distancia entre el punto {self.x,self.y} y el punto {a_point.x,a_point.y} es de: {distance}")
    

punto1 = Punto(2, 3)
punto1.show_point()
punto2= Punto(9, 2)
punto1.distance(punto2)







