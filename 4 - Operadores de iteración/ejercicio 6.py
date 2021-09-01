# Ejercicio 6
# Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
# intervalo y, el segundo, el extremo derecho. Imprime todos los números que se encuentren entre los dos
# números introducidos por el usuario (los extremos incluidos).

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))

for x in range(number1, number2+1):
    print(x, end=",")
