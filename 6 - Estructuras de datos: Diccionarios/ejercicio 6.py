# Ejercicio 6
# Crea un programa que permita al usuario introducir los nombres de los alumnos de una clase y las notas que
# han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario
# cuyas claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
# 1El programa va a pedir el nombre de un estudiante e irá pidiendo sus notas (del 1 al 10) hasta que introduz-
# camos un 0. Al final, cuando el nombre que introduzcamos sea un string vacío, el programa nos mostrará la
# lista de alumnos y la nota media obtenida por cada uno de ellos.
# PISTA: Vas a necesitar la función sum().

estudiantes = {}
nombre = input("Nombre del estudiante: ")

while nombre != "":
    estudiantes[nombre] = []
    nota = int(input("Introduce las notas (de 1 a 10) de {}, una a una: ".format(nombre)))
    while nota != 0:
        estudiantes[nombre].append(nota)
        nota = int(input())
    nombre = input("Nombre del estudiante: ")

    for estudiante in estudiantes:
        print(estudiante, ":", sum(estudiantes[estudiante])/len(estudiantes[estudiante]))

