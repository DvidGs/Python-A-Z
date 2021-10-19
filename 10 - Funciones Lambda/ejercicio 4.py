# Ejercicio 4
# Dada una lista de números enteros, quédate con filter() con los que tengan más de 5 divisores. Necesitarás
# una función que devuelva el número de divisores de un número dado.

def total_divisors(n):
    """
    Calcula el número de divisores un número entero positivo.
    :arg
    :param n: Números entero positivo
    :return
    divisors: Lista de divisores de n
    """
    if type(n) == int and n > 0:
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        return len(divisors)

nums = [49, 1024, 666, 147, 2101, 4]
print(list(filter(lambda n: total_divisors(n) > 5, nums)))
