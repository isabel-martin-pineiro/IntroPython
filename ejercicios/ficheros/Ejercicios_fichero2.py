# Escribe un programa que lea un archivo de texto llamado "frases.txt" 
# que contiene una lista de frases separadas por saltos de línea. 
# El programa debe contar cuántas palabras hay en cada frase y mostrar el número de palabras para cada frase en la pantalla.

fichero = open("frases.txt", "r")
lista = fichero.read().splitlines()
fichero.close()
print(lista)

for each in lista:
    palabras = each.split()
    print(f"'{each}' tiene {len(palabras)} palabras")


