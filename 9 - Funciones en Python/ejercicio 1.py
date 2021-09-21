# Ejercicio 1
# Crea una función que busque todos los divisores del número entero positivo dado por parámetro y devuelva
# una lista con todos los divisores de dicho número.

def divisors(n):
    """
    Calcula los divisores de un número entero positivo.
    Args:
        n: Número entero positivo
    Returns:
        divisors: Lista de divisores de n
    """
    if type(n) == int and n > 0:
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
            return divisors
    else:
        print("Debe introducir un número entero positivo")

print(divisors(2))