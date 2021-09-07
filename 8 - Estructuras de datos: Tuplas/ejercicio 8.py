# Ejercicio 8
# Pide al usuario dos números enteros por teclado. Asegúrate de que el primero es mayor o igual al segundo.
# Realiza la división entera y guarda en una tupla el dividendo, el divisor, el cociente y el resto de la divisón
# entera realizada y muéstrale al usuario el resultado por pantalla.

dividend = int(input("Introduce un numero entero: "))
divisor = int(input("Introduce un numero entero menor o igual al anterior: "))

if divisor > dividend:
    print("El segundo número entero que introduzca debe ser menor o igual al anterior: ")
else:
    print((dividend, divisor, dividend // divisor, dividend % divisor))

