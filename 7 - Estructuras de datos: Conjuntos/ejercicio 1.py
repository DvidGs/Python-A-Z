# Ejercicio 1
# Dado un número entero introducido por teclado, guarda sus divisores en un conjunto y muéstralo.

n = int(input())

if n >= 0:
    divisors = set()
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.add(i)
    print(divisors)
else:
    print("Debe introducir un número entero positivo")