# Ejercicio 6
# Crea una función que devuelva el MCM (mínimo común múltiplo) de 2 números proporcionados por
# parámetro.
# PISTA: Aprovecha la función que calcula el MCD de dos números del ejercicio anterior y la función que
# calcula el valor absoluto de un número.

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

def absolute_value(x):
    """
    Devuelve el valor absoluto de un número real.
    Args:
        x: Número real
    Returns:
        Número real
    """
    if x >= 0:
        return x
    return -x

def mcm(a, b):
    """
    Devuelve el MCM de dos números enteros.
    Args:
         a: Número entero
         b: Número entero
    Returns:
        max: Número entero
    """
    return absolute_value(a * b) // mcd(a, b)

print(mcm(10, 2))
