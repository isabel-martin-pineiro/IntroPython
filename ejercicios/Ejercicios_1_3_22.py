#Escribe una clase Circulo que tenga como atributo el radio. Define una función para calcular su área. 
#Crea un objeto de esta clase y muestra el área de un círculo de radio 5.

# class Circulo():
#     radio = 33
#     def area():
#         return (radio**2)*3.14

# micirculo = Circulo()
# # micirculo.radio = 5
# # print(micirculo.area)


# class Circle:
#     pi = 3.14159
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return round(self.pi, 3) * (self.radius ** 2)


# my_circle = Circle(5)
# print(my_circle.radius)
# print(my_circle.area())

abrir_fichero = open("prueba_apertura.txt", 'w')
abrir_fichero.write("Hola")

abrir_fichero.close()