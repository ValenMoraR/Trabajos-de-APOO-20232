# Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. 
# Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.

# Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
# Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
# Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
# Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.
      
class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

    def depositar(self, cantidad):
        if cantidad > 0:
            self.balance += cantidad
            print(f"Se depositaron ${cantidad}. Nuevo saldo: ${self.balance}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.balance:
            self.balance -= cantidad
            print(f"Se retiraron ${cantidad}. Nuevo saldo: ${self.balance}")
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def aplicar_cuota_manejo(self):
        cuota = self.balance * 0.02
        self.balance -= cuota
        print(f"Se aplicó una cuota de manejo del 2%. Nuevo saldo: ${self.balance}")

    def mostrar_detalles(self):
        print("Detalles de la cuenta:")
        print(f"Número de cuenta: {self.numero_cuenta}")
        print(f"Propietarios: {', '.join(self.propietarios)}")
        print(f"Saldo actual: ${self.balance}")

cuenta = CuentaBancaria("12345", ["Juan", "María"],5000)
cuenta.mostrar_detalles()
cuenta.depositar(500)
cuenta.retirar(200)
cuenta.aplicar_cuota_manejo()
cuenta.mostrar_detalles()
        
