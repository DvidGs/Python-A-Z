# Ejercicio 8
# Dada una lista de números enteros, calcula el número anterior con map().

nums = [-10, 5, 7, -3, 16, -30, 2, 33]
print(list(map(lambda n: n - 1, nums)))