# Ejercicio 5
# Dado un conjunto, crea un programa que nos devuelva el caracter con menor valor ASCII. Debes hacerlo sin
# recurrir a la función min().

valor = {1, 2, "A", "E", "@"}
min = 9999

for i in valor:
    if ord(str(i)) < min:
        min = ord(str(i))

print("El caracter con menor valor ASCII es: ", chr(min))