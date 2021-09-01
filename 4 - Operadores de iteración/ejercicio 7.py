# Ejercicio 7
# Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
# intervalo y, el segundo, el extremo derecho. Imprime la suma de todos los múltiplos de 3 que se encuentren
# entre los dos números introducidos por el usuario (los extremos incluidos). Finalmente, muestra por pantalla
# el resultado de la suma.

number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
result = 0
position = 0

for x in range(number1, number2+1):
    position += 1
    if x % 3 == 0:
        result += x
    if position == number2:
        print("La suma es: ", result)
