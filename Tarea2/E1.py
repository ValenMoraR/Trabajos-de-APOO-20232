# Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.


class Vehiculo:
    def __init__(self, brand, vel_max,mileage):
        self.brand=brand
        self.vel_max= vel_max
        self.mileage= mileage
        

c1= Vehiculo("Ferrari",310,15000)
print (c1.brand,c1.vel_max,c1.mileage)
        
        
        