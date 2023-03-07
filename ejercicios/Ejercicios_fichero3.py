# Escribe un programa que lea un archivo de texto llamado "productos.txt" 
# que contiene una lista de productos y sus precios separados por dos puntos. 
# El programa debe calcular el precio promedio de los productos y mostrar el resultado en la pantalla.

fichero = open("productos.txt","r")
lista = fichero.read().splitlines()
fichero.close()
suma = 0.0
for each in lista:
    elemento_lista = each.split(":")
    suma = suma + float(elemento_lista[1])

promedio = suma / len(lista)
print(round(promedio,2))