# Ejercicio 7
# Haz que un usuario introduzca dos números enteros positivos. Comprueba si el mayor es múltiplo del menor.
# Devuelve por pantalla el resultado en cada caso.

numero_1 = int(input("Numero 1: "))
numero_2 = int(input("Numero 2: "))

if numero_1 > numero_2:
    if numero_1 % numero_2 == 0:
        print("El {} es múltiplo del {}".format(numero_1, numero_2))
    else:
        print("No son múltiplos")
elif numero_2 > numero_1:
    if numero_2 % numero_1 == 0:
        print("El {} es múltiplo del {}".format(numero_2, numero_1))
    else:
        print("No son múltiplos")
else:
    print("No hay número mayor al otro")
