# Crear una clase "CuentaBancaria" que tenga como atributos el número de cuenta (cadena de caracteres)
# y el saldo (float), y como métodos una función para depositar dinero en la cuenta y otra para retirar 
# dinero de la cuenta. La función de retiro debe asegurarse de que el saldo no quede en negativo.

class Cuentabancaria():
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
    def retirar(self,cantidad):
        if  self.saldo >= cantidad:
            self.saldo = (self.saldo - cantidad)
            print(f"Se ha retirado {cantidad} Euros y su saldo es ahora de {self.saldo}")
        else:
            print(f"Operación denegada")

    def depositar(self,cantidad):
        self.saldo = (self.saldo + cantidad)
        print(f"Se ha depositado {cantidad} Euros y su saldo es ahora de {self.saldo}")


c = Cuentabancaria("1234ABC", 300)
opcion = input("Hola! Para retirar dinero escriba 1, para depositar dinero escriba 2")
if opcion == 1:
    cantidad = input("Dame la cantidad que desea retirar")
    c.retirar(cantidad=cantidad)
else:
    cantidad = input("Dame la cantidad que desea depositar")
    c.depositar(cantidad=cantidad)
    
