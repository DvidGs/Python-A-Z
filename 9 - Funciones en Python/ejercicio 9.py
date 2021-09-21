# Ejercicio 9
# Crea una función que dada una lista de palabras por parámetro, devuelva un diccionario que contenga
# cuántas son de longitud par y cuántas de longitud impar.

def even_odd_words(list_of_words):
    """Dada una lista de palabras, devuelve cuántas tienen longitud par e impar
    Args:
        list_of_words: Lista de palabras
    Returns:
        info: diccionario
    """
    info = {"even": 0, "odd": 0}
    for word in list_of_words:
        if len(word) % 2 == 0:
            info["even"] += 1
        else:
            info["odd"] += 1

    return info

