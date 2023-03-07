# Escribe un programa que simule el funcionamiento de una calculadora básica. 
# La calculadora deberá tener los siguientes métodos:

# Sumar dos números.
# Restar dos números.
# Multiplicar dos números.
# Dividir dos números.
# El programa deberá validar que el usuario ingrese dos números válidos 
# (deben ser números enteros o números de punto flotante) 
# y permitir al usuario realizar las operaciones mencionadas anteriormente.

class Calculadora():
    def suma_lista(self, lista: list):
        suma_lista = 0
        for each in lista:
            suma_lista = suma_lista + each 
        return suma_lista 
    def suma(self, a, b):
        suma = a + b
        return suma 
    def resta(self, a, b):
        resta = a - b
        return resta
    def multiplicar(self, a, b):
        multiplicar = a * b
        return multiplicar 
    def dividir(self, a, b):
        dividir = a / b
        return dividir 

calculadora = Calculadora()
a = float(input(f"Dame un número: "))
b = float(input(f"Dame otro número: "))

print(calculadora.suma(a,b))