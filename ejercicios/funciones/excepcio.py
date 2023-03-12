# Escribe una función en Python llamada "dividir" que acepte dos argumentos, 
# "num" y "den", y devuelva el resultado de la división num/den. 
# La función deberá manejar la excepción de división por cero y devolver un mensaje de error en tal caso.

def dividir(num, den):
    try:
        resultado = num / den
        return resultado
    except ZeroDivisionError:
        return "Error: no se puede dividir entre cero"

resultado1 = dividir(10, 2)
print(resultado1) # Imprime: 5.0

resultado2 = dividir(10, 0)
print(resultado2) # Imprime: "Error: no se puede dividir entre cero"
