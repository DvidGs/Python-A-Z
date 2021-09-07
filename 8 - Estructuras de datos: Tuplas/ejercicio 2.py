#Ejercicio 2
#Dado un año proporcionado por el usuario, crea una tupla de dos elementos cuya primera entrada sea el año
#y, la segunda entrada, el horóscopo chino correspondiente.

year = int(input("indroduce un año: "))

horoscopes = ["Mono", "Gallo", "Perro", "Cerdo", "Rata", "Buey",
              "Tigre", "Conejo", "Dragón", "Serpiente", "Caballo", "Cabra"]

horoscope = horoscopes[year % 12]
result = (year, horoscope)
print(result)

