# Ejercicio 8
# Pídele al usuario cuántos números va a introducir. Con un bucle for, solicítale esa cantidad de números y
# calcula su producto.

numbers = int(input("¿Cuántos números va a introducir: "))
producto = 1

for x in (1, numbers):
    number = int(input("{}) Ingrese un número: ".format(x)))
    producto *= number
    if x == numbers:
        print("Producto: ", producto)
