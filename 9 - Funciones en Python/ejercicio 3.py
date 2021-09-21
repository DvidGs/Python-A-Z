# Ejercicio 3
# Crea una función que dado un número devuelva su valor absoluto. Recuerda,
# 
# |x| =
# x si x >= 0
# −x si x < 0

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

print(absolute_value(-5))