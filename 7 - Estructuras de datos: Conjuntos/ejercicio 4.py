# Ejercicio 4
# Dado un conjunto, crea un programa que nos devuelva el caracter con mayor valor ASCII. Debes hacerlo sin
# recurrir a la función max().

valor = {1, 2, "A", "E", "@"}
max = -9999

for i in valor:
    if ord(str(i)) > max:
        max = ord(str(i))

print("El caracter con mayor valor ASCII es: ", chr(max))

