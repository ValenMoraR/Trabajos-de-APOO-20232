# Cree una clase Rectángulo la cual contiene dos atributos de instancia 
# que representan los puntos que definen sus esquinas. 
# Agregue métodos a la clase Rectángulo para calcular su perímetro, 
# calcular su área e indicar si el rectángulo es un cuadrado.


class Rectangulo:
    def __init__(self, esq_sup_izq, esq_inf_der):
        self.esq_sup_izq= esq_sup_izq
        self.esq_inf_der= esq_inf_der
        
    def perimetro(self):
        base= self.esq_inf_der[0]- self.esq_sup_izq[0]
        altura= self.esq_inf_der[1]- self.esq_sup_izq[1]
        return 2*(base + altura)
    
    def area(self):
        base = self.esq_inf_der[0] - self.esq_sup_izq[0]
        altura = self.esq_inf_der[1] - self.esq_sup_izq[1]
        if base == altura:
            return "Es un cruadrado"
        else:
            return base * altura
        
esq_sup_izq=(1,4)
esq_inf_der=(5,1)

rectangulo= Rectangulo(esq_sup_izq,esq_inf_der)
print(rectangulo.perimetro())
print(rectangulo.area())