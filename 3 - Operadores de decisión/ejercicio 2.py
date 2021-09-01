# Ejercicio 2
# Haz que un usuario introduzca su nombre y evalúa con operadores if y else si dicho nombre tiene una
# longitud mayor a 10 caracteres o no. Devuelve por pantalla el resultado en cada caso.

name = input("Introduzca su nombre:")

print("Su nombre supera los 10 caracteres") if len(name) > 10 else print("Su nombre no supera")