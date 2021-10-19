# Ejercicio 1
# Crea una función lambda que dado un número entero multiplique por su anterior y su siguiente. Por ejemplo,
# si proporcionamos n = 3, nos tendrá que devolver 2 · 3 · 4 = 24.


plus_before_after = lambda n: (n - 1) * n * (n + 1)

print(plus_before_after(3))