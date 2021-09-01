# Ejercicio 3
# Haz que el usuario introduzca precios por teclado (si introduce 0, entonces es que ha finalizado). Si el usuario
# pasa de 200€, entonces ya no debe poder introducir más precios pues se ha pasado de presupuesto. Sea cual
# sea el resultado (o bien el precio final o bien que no tiene más presupuesto), indícaselo por pantalla al usuario.

price = 0.0
total = 0.0
while True:
    price = float(input("Precio: "))
    total += price
    if total > 200:
        print("Sobrepaso el presupuesto ")
        break
    elif price == 0:
        print("Total: ", total)
        break
    else:
        continue
