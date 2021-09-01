# Ejercicio 3
# Escribe un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar
# el artículo y su precio por unidad. El artículo será la clave y el valor el precio, hasta que el usuario decida
# terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

lista = {}
articulo = str(input("Articulo: "))

while articulo != "":
    lista[articulo] = float(input("Precio: "))
    articulo = str(input("Articulo: "))
print("")
for articulo, val in lista.items():
    print("|" + " " * (20 - 2 -len(articulo)) + articulo +
          " | " + str(val) + " " * (9 - len(str(val))) + "|")



