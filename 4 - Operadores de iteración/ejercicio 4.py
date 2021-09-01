# Ejercicio 4
# Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, calcula
# cuántos números positivos y cuántos negativos ha introducido y muéstraselo al final.

number = int
positive = 0
negative = 0
while number != 0:
    number = int(input("Número: "))
    if number >= 1:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        print("Números positivos", positive)
        print("Números negativos", negative)
        continue
