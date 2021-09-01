# Ejercicio 6
# Fusiona lo hecho en los ejercicios 4 y 5 para que
# 1. Un usuario introduzca dos números enteros por pantalla.
# 2. Comprobar si el primer número es mayor o igual al segundo número introducido por el usuario. Devolver
# por pantalla en que caso nos encontramos.
# 3. Hacer la división entera pertinente en cada caso.
# 4. Si la división es entera, entonces devolver por pantalla el cociente e indicar que la división es entera.
# Si la división no es entera, entonces devolver por pantalla el cociente y el resto e indicar que la división
# realizada no es entera.

uno = int(input("Número uno:"))
dos = int(input("Número dos:"))

print("El primer número es mayor o igual al segundo") if uno >= dos else print("El segundo número es mayor al primero")

if uno >= dos:
    resultado = uno % dos
    if resultado != 0:         # Una división es entera cuando el resto es distinto de cero.
        print("La division es entera")
    else:
        cociente = uno / dos
        print("El cociente de la división es: {}\nSu resto es: {}".format(cociente, resultado))
        print("No es Entera")