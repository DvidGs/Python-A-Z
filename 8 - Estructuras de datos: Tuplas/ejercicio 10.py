# Ejercicio 10
# Pide al usuario números complejos. Para cada número, crea una tupla donde la primera entrada sea dicho
# número complejo, la segunda, su opuesto y, la tercera, su conjugado.

z = complex(float(input("Introduce la parte real de un número complejo: ")),
            float(input("Introduce la parte imaginaria de un número complejo: ")))

print((z, -z, z.conjugate()))