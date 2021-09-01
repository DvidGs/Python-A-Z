# Ejercicio 4
# Crea un programa que lea una palabra, la guarde en una lista y compruebe si se trata de un palíndromo.
texto = str(input("palabra: "))
lista = []
l = 0
for x in texto:
    for d in x:
        lista.append(d)
        l += 1
        if len(texto) == l:
            if lista == lista[::-1]:
                print("Es Palíndromo")
            else:
                print("No es Palíndromo")


