# Ejercicio 1
# Crea un programa que pida un número entero positivo por teclado y que cree un diccionario cuyas claves
# sean desde el número 1 hasta el número indicado. Los valores de cada clave serán las propias claves elevadas
# al cubo.

numero = int(input("Agregue un número: "))
clave = {}

for c in range(0, numero):
    clave[c+1] = (c+1)**3
print(clave)


