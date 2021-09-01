# Ejercicio 4
# Haz que un usuario introduzca dos números enteros positivos. Comprueba si el primer número introducido
# por el usuario es mayor o igual que el segundo número introducido por el usuario. Devuelve por pantalla el
# resultado en cada caso.
# PISTA: Asegúrate de hacer uso de la función int() donde pertoque.

uno = int(input("Número uno:"))
dos = int(input("Número dos:"))

print("El primer número es mayor o igual al segundo") if uno >= dos else print("El segundo número es mayor al primero")

