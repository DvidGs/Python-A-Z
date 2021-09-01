# Preguntas de esta tarea
# ¡Ayuda a Pyratilla a crear un diccionario llamado info_pyrates que contenga para cada miembro de la tripulación de los Pyrates un diccionario con la edad (age) y la ocupación (occupation) de cada uno.
#
# Ayuda a Pyratilla a mostrar los datos de cada uno de los miembros de su tripulación como se muestra a continuación:

#Pyratilla es el capitán del barco y tiene 16 años


info_pyrates = {"pyratilla": {"edad": 17, "ocupacion": "capitan"},
                "pyo": {"edad": 1, "ocupacion": "loro"}}

for miembro in info_pyrates:
    print("{} es el {} del barco y tiene {} años". format(miembro, info_pyrates[miembro]["ocupacion"], info_pyrates[miembro]["edad"]))