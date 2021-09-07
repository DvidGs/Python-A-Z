weapons = [("Flecha", 20), ("Espada, 5"), ("Daga", 15), ("Puñal", 12),
          ("Martillo", 7), ("Hacha", 10), ("Maza", 3), ("Machete", 8)]

enemies = 8
print("Hay que derrotar a {} comebarcos\n".format(enemies))
for weapon, hits in weapons:

    if weapon in ["Flecha", "Espada", "Daga", "Maza"]:
        articulo = "la"
    else:
        articulo = "el"

    for i in range(hits):
        if i + 1 == 1:
            print("Le damos al enemigo {} vez con {} {}".format(i + 1, articulo, weapon.lower()))
        else:
            print("Le damos al enemigo {} veces con {} {}".format(i + 1, articulo, weapon.lower()))

        enemies -= 1
        if enemies > 0:
            print("\n{} {} comebarcos sin derrotar\n".format("Queda" if enemies == 1 else "Quedan", enemies))

print("\n¡Todos los comebarcos han sido eliminados!")

unvisted_islands.remove("Isla Arrecife")
visited_islands.add("Isla Arrecife")

coins = [("moneda"), ("Alegre"), ("amarilla"),
         ("coralina"), ("Arrecife"), ("azul"),
         ("rupia"), ("Verde"), ("verde"),
         ("chuche"), ("Golosa"), ("rosa"),
         ("lista"), ("Lejania"), ("roja"),
         ("gema"), ("Espesura"), ("lila"),
         ("corona"), ("Torva"), ("naranja"),]

for coin, island, color in coins:
    print("En la isla {} se usa la {} de color {}".format(island, coin, color))

