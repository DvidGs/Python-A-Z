# Ejercicio 2
# Crea un programa que dado un conjunto, nos devuelva su mínimo. Debes hacerlo sin recurrir a la función
# min().

myset = {1, 2, 3, 4, -1, -2, 3}
min = 50

for i in myset:
    if i < min:
        min = i

print("El mínimo de {} es {}".format(myset, min))

