# Escribe una función en Python llamada "imprimir_numeros" que acepte un argumento "limite" 
# y que imprima todos los números enteros desde 1 hasta el "limite", ambos incluidos. 
# Si el límite no es un número entero, la función deberá manejar la excepción 
# y devolver un mensaje de error en tal caso.

def imprimir_numeros(limite):
    i = 0
    try:
        limite = int(limite)
        while i <= limite:
            print(i)
            i = i + 1
    except ValueError:
        print("El valor no es un entero")
        
limite = input("Dame un número: ")
imprimir_numeros(limite)    
    
        
