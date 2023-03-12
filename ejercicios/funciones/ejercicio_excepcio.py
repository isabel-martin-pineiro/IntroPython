# Escribe una función en Python llamada "calcular_precio_final" que acepte dos argumentos, 
# "precio_base" y "descuento", y devuelva el precio final después de aplicar el descuento. 
# La función deberá manejar la excepción de que el descuento sea mayor que el precio base 
# y devolver un mensaje de error en tal caso.

def calcular_precio_final(precio_base, descuento):
    try:
        if descuento > precio_base:
            raise ValueError("El descuento no puede ser mayor que el precio")
        resultado = precio_base - descuento
        return resultado
    except ValueError as error:
        return str(error)
    
resultado1 = calcular_precio_final(10,2)
print(resultado1)

resultado2 = calcular_precio_final(2, 10)
print(resultado2)