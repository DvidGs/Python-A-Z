# Ejercicio 5
# Haz que el usuario introduzca números por teclado. Mientras el usuario no introduzca el 0, pídele otro
# número. Cuando el usuario introduzca el 0, muéstrale la media aritmética de los números que ha introducido.

number = int
x = 0
n = 0
while number != 0:
    number = int(input("Ingrese un número: "))
    x += number
    n += 1
    if number == 0:
        result = x / (n-1)
        print("Media Aritmética: ", int(result))

