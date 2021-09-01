# Ejercicio 9
# Haz que el usuario introduzca su edad y el año actual. Imprime todos los años que han pasado desde su año
# de nacimiento hasta el año actual (ambos incluidos).

edad = int(input("Edad: "))
anho = int(input("Año actual: "))
nacimiento = anho - edad

for x in range(nacimiento, anho+1):
    print(x, end=",")