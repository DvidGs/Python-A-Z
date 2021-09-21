# Ejercicio 7
# Crea una función que dada una palabra devuelva si es palíndroma.

def is_palindrome(word):
    """
    Devuelve si la palabra word es palídroma.
    Args:
         word: Palabra
    Return:
        isPalindrome: Booleno
    """
    word = word.lower()
    l = []
    isPalindrome = True
    for c in word: l.append(c)
    n = len(l)
    for i in range(int(n / 2)):
        if l[i] != l[n - (i + 1)]: isPalindrome = False
    return isPalindrome