# Ejercicio 1
# Pide al usuario el número de números enteros que va a introducir por teclado. Para cada uno de esos
# números, crea una tupla donde la primera entrada sea el número entero y, la segunda, la palabra “par” o
# “impar” según la paridad del número entero. Muestra la tupla recién creada al usuario.

n = int(input("¿Cuántos números enteros vas a introducir? "))
nums = []

for _ in range(n):
    isEven = False
    num = int(input())
    if num % 2 == 0:
        isEven = True
    nums.append((num, "par" if isEven else "impar"))
print(nums)

