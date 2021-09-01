# Ejercicio 3
# Crea un programa que lea un string y guarde en una lista todas las consonantes.

texto = '"Felicitacion", "Huelga", "Luminoso", "Aire", "A", "U", "rr"'
lista = []
consonante = False
cont = 0

#consonantes = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "Ñ", "P", "Q", "R", "S", "T", "V", "X", "Z", "W", "Y"]
for t in texto:
    #print(t)
    for c in t:
        c = c.upper()
        cont += 1
        lista += c
        print(c)
        if c == "B" or c == "C" or c == "D" or c == "F" or c == "G" or c == "H" \
                or c == "J" or c == "K" or c == "L" or c == "M" or c == "N" \
                or c == "Ñ" or c == "P" or c == "Q" or c == "R" or c == "S" \
                or c == "T" or c == "V" or c == "X" or c == "Z" or c == "W" or c == "Y":

            consonante = True

        elif consonante == True and len(texto) == t:
            print(lista)
            consonante = False
            cont = 0
        else:
            continue


