# Ejercicio 9
# Pide al usuario números entre 0 y 360. Para cada número, crea una tupla donde la primera entrada sea
# dicho número y, la segunda, la medida angular correspondiente en radianes. Recuerda, 360 ◦ = 2πrad. En
# este caso, utiliza π = 3.141592653589793

degree = float(input("Introduce un número del intervalo [0, 360] "))
print((degree, degree * 2 * 3.141592653589793 / 360))

