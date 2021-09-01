# Ayuda a Pyratilla a que el anuncio le quede bien:
#
# El título debe estar todo en mayúsculas
# El principio de cada frase debe estar en mayúscula
# Cada vez que hay un cambio de variable, debe haber un salto de línea
# El nombre de Pyratilla debe estar en mayúscula
# Pista: puede que te sea más fácil si guardas las dos frases de la variable message en dos variables diferentes y una vez las tengas listas, las vuelves a unir.


title = "se busca tripulante"
message = "se ofrece puesto en la tripulación del capitán pyratilla para llevar a cabo labores de marinero. "
message2 = "comida y bebida garantizada a lo largo de toda la aventura."
contact = "para más información, ir al puerto y buscar al capitán pyratilla, ya famoso en este pueblo costero (evitar preguntar en el casino)."

print(title.upper() + "\n" + message.replace("pyratilla", "PYRATILLA") + message.capitalize() + message2.capitalize() + "\n" + contact.replace("pyratilla", "PYRATILLA") + contact.capitalize())


