# 99 Bottles of Rum on the Wall
# De tantas solicitudes que ha recibido, Pyratilla no cabe en sí de la emoción y se pone a cantar
#
# "99 bottles of rum on the wall, 99 bottles of rum.
# Take one down, pass it around, 98 bottles of rum on the wall.
# 98 bottles of rum on the wall, 98 bottles of rum.
# Take one down, pass it around, 97 bottles of rum on the wall..."

# Ayuda a Pyratilla a cantar la canción al completo con un bucle while.
# Ayuda a Pyratilla a cantar la canción al completo con un bucle for.


'''
bottles = 99
while bottles != 1:
    print("{} bottles of rum on the wall, {} bottles of rum.".format(bottles, bottles))
    bottles -= 1
    print("Take one down, pass it around, {} bottles of rum on the wall.".format(bottles))
'''


bottles = 99
for p in range(bottles, 1, -1):
    print("{} bottles of rum on the wall, {} bottles of rum.".format(p, p))
    p -= 1
    print("Take one down, pass it around, {} bottles of rum on the wall.".format(p))

