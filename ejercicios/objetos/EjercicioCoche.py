# Enunciado: Queremos crear una clase llamada "Coche" que tenga atributos 
# como marca, modelo, año y kilometraje, así como métodos para calcular 
# la depreciación y la cantidad de combustible necesaria para un viaje.

class Coche():
    def __init__(self, marca, modelo, año, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
    
    def depreciacion(self):
        if self.año >= 2021:
            return 0
        elif self.año >=2018:
            return 1.2
        elif self.año >= 2014:
            return 1.4
        else:
            return 2.5


    def combustible(self, distancia):
       precio_km = 1.5
       return distancia * precio_km
    
distancia = float(input("¿Cuánta distancia recorrerás?: "))
marca = input("¿De qué marca es tu coche?: ")
modelo = input("¿Qué modelo de coche tienes?: ")
año = int(input("¿En qué año compraste tu coche?"))
kilometraje = int(input("¿Qué kilometraje tiene tu coche?: "))

coche = Coche(marca, modelo, año, kilometraje)
print(f"Tienes un coche de marca {coche.marca}, modelo {coche.modelo}, con {coche.kilometraje} kilometraje.")
print(f"La depreciación es de {coche.depreciacion()}")
print(f"El combustible necesario es de {coche.combustible(distancia)} litros.")
