# Ejercicio 8
# Haz que un usuario introduzca una palabra y comprueba si dicha palabra empieza por mayúscula. Devuelve
# por pantalla el resultado en cada caso.

x = input("Introduce una palabra: ")

if x[0] == x[0].upper():
    print("La primera letra {} empieza por mayúscula".format(x[0]))
else:
    print("La primera letra no está en mayúscula")

