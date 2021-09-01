# Ejercicio 6
# Crea un programa que lea un entero, n, de teclado y construya una matriz de tamaño n × n. Cada posición
# debe contener su orden en la matriz (desde 0 hasta n 2 − 1. Por ejemplo, si n es 3, deberá crearse la matriz
# [0, 1, 2]
# [3, 4, 5]
# [6, 7, 8]

numero = int(input("Agregue un numero: "))
contador = 0
fila = 0
lista = []
for x in range(0, numero*numero):
    #for x2 in range(1, numero+1):
    lista.append(contador)
    contador += 1
    fila += 1
    if fila == numero:
        print(lista)
        lista.clear()
        fila = 0


