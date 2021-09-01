# Ejercicio 1
# Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, muestra
# si el número introducido es par o impar.

x = 1
while x != 0:
    x = int(input("Introduzca un numero: "))
    if x % 2 == 0:
        print('El número', x, 'es par.')
    else:
        print('El número', x, 'es impar.')