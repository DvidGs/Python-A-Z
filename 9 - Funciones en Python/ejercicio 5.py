# Ejercicio 5
# Crea una función que devuelva el MCD (máximo común divisor) de 2 números proporcionados por parámetro.
# PISTA: Aprovecha la función que calcula el mayor entre dos números dados. También necesitarás una función
# que calcula el menor entre dos números dados.

def bigger(a, b):
    """
    Devuelve el mayor numero de 2 números reales dados.
    Args:
        a: Número real
        b: Número real
    Return:
        Número real
    """
    if a >= b:
        return a
    return b

def lower(a, b):
    """
    Devuelve el menor número de 2 números reales dados.
    Args
        a: Número real
        b: Número real
    Returns:
        Número real
    """
    if a <= b:
        return a
    return b

def mcd(a, b):
    """
    Devuelve el MCD de dos números enteros.
    Args:
         a: Número entero
         b: Número entero
    Returns:
        max: Número entero
    """
    r = 0
    max = bigger(a, b)
    min = lower(a, b)

    while(min > 0):
        r = min
        min = max % min
        max = r
    return max

print(mcd(10, 2))

