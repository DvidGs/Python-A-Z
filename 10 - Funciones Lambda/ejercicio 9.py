# Ejercicio 9
# Dada una lista de números reales, ordénalos con sorted() por valor absoluto de menor a mayor.

def absolute_value(x):
    """
    Devuelve el valor absoluto de un número real.
    :arg
    :param x: Número real
    :return: Número real
    """
    if x >= 0:
        return x
    return -x

nums = [50, -21.5, 66.6, -4.5, 1.7, -5.4]
print(sorted(nums, key=absolute_value))