# Ejercicio 5
# Haz que un usuario introduzca dos números enteros positivos. Suponiendo que el primer número introducido
# por el usuario es mayor o igual al segundo número introducido por el usuario, comprueba que la división del
# primer número entre el segundo número es entera.
# En caso de la división ser entera, devuelve el cociente por pantalla e indica que la división en efecto es entera.
# En caso de la división no ser entera, devuelve el cociente y el resto por pantalla e indica que la división entre
# los dos números no es entera.

## Divisón exacta 24/6
## División entera 17/5

uno = int(input("Número uno:"))
dos = int(input("Número dos:"))

if uno >= dos:
    resultado = uno % dos
    if resultado != 0:         # Una división es entera cuando el resto es distinto de cero.
        print("La division es entera")
    else:
        cociente = uno / dos
        print("El cociente de la división es: {}\nSu resto es: {}".format(cociente, resultado))
        print("No es Entera")
