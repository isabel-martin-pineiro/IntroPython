# Escribe un programa en Python que solicite al usuario el ingreso de los nombres, 
# edades y alturas de dos personas y los almacene en dos objetos diferentes. 
# Luego, el programa deberá imprimir la información de ambas personas, incluyendo su nombre, edad y altura.

class Persona():
    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

persona1_nombre = input(f"Dame tu nombre: ")
persona1_edad = int(input(f"Dame tu edad: "))
persona1_altura = float(input(f"Dame tu altura: "))

persona1 = Persona(persona1_nombre, persona1_edad, persona1_altura)

persona2_nombre = input(f"Dame tu nombre: ")
persona2_edad = int(input(f"Dame tu edad: "))
persona2_altura = float(input(f"Dame tu altura: "))

persona2 = Persona(persona2_nombre, persona2_edad, persona2_altura)

print(f"Mi nombre es {persona1.nombre}, tengo {persona1.edad} años y mido {persona1.altura} metros.")

print(f"Mi nombre es {persona2.nombre}, tengo {persona2.edad} años y mido {persona2.altura} metros.")
