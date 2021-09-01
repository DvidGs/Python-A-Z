# Ejercicio 10
# Haz que el usuario introduzca un número entero. Muestra un cuadrado y luego un triángulo rectángulo de
# lado y altura, respectivamente, el número entero introducido. Por ejemplo, si el usuario introduce como
# número 5, se deberá mostrar:

# *           * * * * *
# * *         * * * * *
# * * *       * * * * *
# * * * *     * * * * *
# * * * * *   * * * * *

numero = int(input("Introduzca un número entero: "))
espacio = numero

for c in range(1, numero+1):
    triangulo = "*" * c
    cuadrado = "*" * numero
    print(triangulo + espacio*" " + cuadrado)
    espacio -= 1