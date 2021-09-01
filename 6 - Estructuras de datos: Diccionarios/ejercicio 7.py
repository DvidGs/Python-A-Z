# Ejercicio 7
# Crea un programa que pida un número entero positivo por teclado y que cree un diccionario cuyas claves
# sean desde el número 1 hasta el número indicado. Los valores de cada clave serán tantos símbolos "*" como
# indique la clave.


numero = int(input("numero entero poditivo: "))

diccionario = {}
for i in range(1, numero + 1):
    diccionario[i] = "*" * i
print(diccionario)