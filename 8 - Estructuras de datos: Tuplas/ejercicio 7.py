# Ejercicio 7
# Crea una lista de 20 tuplas de tamaño 2. La primera entrada será un número entero entre 1 y 20 y la segunda
# entrada contendrá una lista con los 10 primeros múltiplos del número entero correspondiente. Por último,
# muestra las tablas de multiplicar del 1 al 20 con el formato “1 x 1 = 1”.

multiplicacion_tables = []

for i in range(1, 21):
    multiplicacion_tables.append((i, [i * j for j in range(1, 11)]))

for item in multiplicacion_tables:
    print("Tabla Del {}".format(item[0]))

for multiple in item[1]:
    print("{} x {} = {}".format(item[0], item[1].index(multiple) + 1, multiple))

