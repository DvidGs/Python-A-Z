# Ejercicio 9
# Haz un usuario introduza una letra y comprueba si se trata de una vocal. Si el usuario introduce un string
# de más de un carácter, infórmale de que no se puede procesar el dato, pues debe tener como máximo tamaño
# 1.
# PISTA: Convierte la letra introducida a minúsculas para tener que realizar menos comprobaciones

letra = input("Introduce una letra: ")
letra = letra.lower()

if len(letra) == 1:
    if letra[0] == "a" or letra[0] == "e" or letra[0] == "i" or letra[0] == "o" or letra[0] == "u":
        print("Empieza por una vocal")
    else:
        print("No empieza por vocal")
elif len(letra) > 1:
    print("no se puede procesar el dato 'Solo es una letra'")





