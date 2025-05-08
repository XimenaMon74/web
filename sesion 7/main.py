# Escribe esta linea de código
print("Bienvenidos al entrenamiento con python, vamos a trabajar al máximo esta sesión")

"""
    Descuento en una compra:
    Si compras más de $100, obtienes un descuento del 20%
    Pide el monto de la compra y muestra el precio final
"""

# Pedir datos por teclado al usuario int (entero) float (decimal) str (cadenas de caracteres) bool (unos o ceros)

compra = float(input("Por favor, digita el valor de tu compra: ")) 
# Si compras más de $1000, tú tienes un descuento del 20%
# Siempre que la salida tenga más de un camino de resolución, debo de implementar condicionales
# Operadores combinados
# Operadores de asignación =, operadores aritmeticos + - * /, operadores logicos and y, or o, not
# Operadores de comparación ==,!=,>,<,>=,<=

if compra > 1000: 
    descuento = compra * 0.2
    compra -= descuento
    #compra = compra - descuento
    print(f"el descuento es de {descuento}, por lo tanto su valor a pagar es: {compra}")