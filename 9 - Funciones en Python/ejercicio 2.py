# Ejercicio 2
# Crea una función que dados dos números reales por parámetro, devuelve el mayor.

def bigger(a, b):
    """
    Devuelve el mayor número de 2 números reales dados.
    Args:
        a: Número real
        b: Número real
    Returns:
        Número real
    """
    if a >= b:
        return a
    return b

print(bigger(5, 10))