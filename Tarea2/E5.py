#5 # Cree una clase Circulo que tenga las propiedades centro y radio, 
# las cuales se inicializan con parámetros en el constructor. 
# Defina métodos en la clase para calcular el área, 
# el perímetro e indicar si un punto pertenece al círculo o no.

import math

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * math.pi * self.radio
    
    def punto_pertenece(self, punto):
        distancia = math.sqrt((punto[0] - self.centro[0]) ** 2 + (punto[1] - self.centro[1]) ** 2)
        return distancia <= self.radio

centro = (0, 0)
radio = 5
circulo = Circulo(centro, radio)

print("Área:", circulo.calcular_area())
print("Perímetro:", circulo.calcular_perimetro())

punto1 = (3, 4)
punto2 = (6, 6)

print("El punto", punto1, "pertenece al círculo:", circulo.punto_pertenece(punto1))
print("El punto", punto2, "pertenece al círculo:", circulo.punto_pertenece(punto2))
