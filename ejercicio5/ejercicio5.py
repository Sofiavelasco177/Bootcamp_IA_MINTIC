#Escribe esta linea de codigo:
print("Bienvenidos al entrenamiento con python, vamos a disfrutar al máximo esta sesión")
"""
Descuento en una compra:
Si compras más de $1000, obtienes un descuento del 20%
Pide el monto de la compra y muetra el precio final

"""
# Pedir datos por teclado al usuario int entero float decimales str cadenas de caracteres bool booleanos

compra = float(input("Digite el valor de la compra: "))

# Si compras más de $1000, obtienes un descuento del 20%
# Siempre que la salida tenga más de un camino de resolución, debo implemantar condicionales

# operadores combinados
# operadores de asignación =, operadores aritméticos + -* / , operadores lógicos and y, or o, not,
# #operadores de comparación == , != , >, <, >=, <=

if compra > 1000:
    descuento = compra * 0.2
    #compra = compra - descuento # operador de asignación
    compra -= descuento # operador de asignación compuesto
    print (f"El descuento es de {descuento}, por lo tanto su valor a pagar es: {compra}")