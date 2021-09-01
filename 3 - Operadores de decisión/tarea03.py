# Pyratilla hizo un formulario para que los interesados en formar parte de su tripulación rellenaran y así poder evitarse más de una entrevista innecesaria.

#Ahora es momento de filtrar las convocatorias:

#El nombre debe empezar por mayúscula. Si es un nombre compuesto, entonces todos deben empezar por mayúscula.
#La edad debe ser mayor o igual a 16 y menor o igual a 40.
#El hobby indicado debe tener más de 10 caracteres.
#La casilla del sueño no puede haber sido dejada en blanco.
#Ayuda a Pyratilla a crear este filtro para descartar solicitudes que no cumplan estos requisitos.


nombre = input("nombre: ")
nombre = nombre.title()
edad = int(input("Edad: "))
hobby = input("Hobby: ")
sueno = input("sueño: ")

if edad >= 16 and edad <= 40:
    if len(hobby) > 10:
        if sueno != " ":
            print("Es un buen candidato {}, {} años, {}, {}".format(nombre, edad, hobby, sueno))
        else:
            print("La casilla del sueño no puede haber sido dejada en blanco")
    else:
        print("hobby indicado debe tener más de 10 caracteres")
else:
    print("No cumple la edad")