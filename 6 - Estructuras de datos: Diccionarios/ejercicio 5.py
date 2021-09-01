# Ejercicio 5
# Crea un programa que lea números enteros hasta que introduzca el 0 y devuelva un diccionario con la
# cantidad números pares e impares introducidos.

n = int(input("Número entero: "))
par = 0
total = 0

while n != 0:
    if n % 2 == 0:
        par +=1
    total += 1
    n = int(input("Número entero: "))

nums = {"par": par, "impar": total - par}
print(nums)

