# ¡Ayuda a Pyratilla a crear un método llamado convert_to_coins que dada una cantidad y el nombre de la moneda, realice la conversión a monedas de Isla Alegre!
#
# Encontrarás la respuesta adjunta en el video explicativo con la solución
#
# ¡Ayuda a Pyratilla a aplicar dicha función para sumar al total de sus monedas, coins, todas las adquiridas en el botín de Isla Arrecife!
#
# Encontrarás la respuesta adjunta en el video explicativo con la solución
#
# ¡Ayuda a Pyratilla a crear esa nueva función, llamada currency_converter, que por parámetro reciba la cantidad, la divisa de partida y la divisa a la que quiere convertirse!
#
# Encontrarás la respuesta adjunta en el video explicativo con la solución
#
# Ayuda a Pyratilla a eliminar Isla Espesura de unvisited_islands y añadirla al conjunto visited_islands de la entrada 08 de su diario.
#
# Encontrarás la respuesta adjunta en el video explicativo con la solución
#
# Ayuda a Pyratilla a crear la función de la inscripción la cual debe de leer como parámetro un texto (un solo string) y como resultado debe devolver el número de palabras de longitud par y el número de palabras de longitud impar que hay en dicho texto, en una tupla donde la primera entrada sea el número de palabras pares y la segunda, el número de palabras impares. Además, deberás aplicarla al texto que se lee en la inscripción y decir cuántas palabras pares y cuántas impares hay. Solo así conseguirás abrir el cofre.
#
# Encontrarás la respuesta adjunta en el video explicativo con la solución


coins = 450000

def convert_to_coins(x, name = "moneda"):
    if name.lower() == "moneda":
        return x

    if name.lower() == "coralina":
        return x * 0.75

    if name.lower() == "rupia":
        return x * 0.55

    if name.lower() == "chuche":
        return x * 1.3

    if name.lower() == "lita":
        return x * 2.15

    if name.lower() == "gema":
        return x * 1.7

    if name.lower() == "corona":
        return x * 0.95

    print("Asegúrate de que el nombre de la que has introducido es correcto")

monedas = 1050
coralinas = convert_to_coins(1310, "coralina")
rupias = convert_to_coins(2025, "rupia")
chuches = convert_to_coins(1520, "cuche")
litas = convert_to_coins(970, "litia")
gemas = convert_to_coins(1975, "gema")
coronas = convert_to_coins(1760, "corona")

coins += monedas + coralinas + rupias + chuches + litas + gemas + coronas
print("El total de monedas de pyratilla y su tripulación es de", coins)


def currency_converter(x, coin_from, coin_to="moneda"):
    return convert_to_coins(x, coin_from) / convert_to_coins(1, coin_to)


def num_even_odd_words(text):
    total_even, total_odd = 0, 0

    words_list = text.split(" ")
    for word in words_list:
        if len(word) % 2 == 0:
            total_even += 1
        else:
            total_odd += 1
        return (total_even, total_odd)

even, odd = num_even_odd_words(texto)
print("En la inscripción hay {} palabras pares y {} impares".format(even, odd))

