# Crear una clase "Persona" que tenga como atributos el nombre y la edad, y como método una función 
# que imprima en pantalla la frase "Hola, mi nombre es {nombre} y tengo {edad} años".

class PorFavorEmiteMensaje():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        # falta la edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")
        # falta mensaje (print)


# Crear un objeto y llamar a la función presentarse()
p1 = PorFavorEmiteMensaje("Maria", 25)
