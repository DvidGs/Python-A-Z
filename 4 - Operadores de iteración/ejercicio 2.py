# Ejercicio 2
# Haz que el usuario introduzca una palabra y una letra por teclado. Comprueba si la palabra contiene la
# letra o no e indícaselo al usuario por pantalla.

pa = str(input("Introduzca una palabra: "))
le = str(input("Introduzca una letra: "))
cont = 0
for x in pa:
    cont += 1
    if x == le:
        #print(x, end="")
        print("La palabra 'Si' contiene la letra", le)
        break
    elif cont >= len(pa):
        print("La palabra 'No' contiene la letra", le)
    else:
        continue
