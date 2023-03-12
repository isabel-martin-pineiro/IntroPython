# Escribe un programa que lea un archivo de texto llamado "numeros.txt" 
# que contiene una lista de números enteros separados por comas. 
# El programa debe sumar todos los números y mostrar el resultado en la pantalla.

fichero = open("numeros.txt","r")
lista = []
for linea in fichero:
    lista = linea.split(",")
fichero.close()
suma = 0
for each in lista:
    suma = int(each) + suma
print(suma)
