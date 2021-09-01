# Ejercicio 2
# Escribe un programa que pregunte al usuario su nombre, edad y teléfono y lo guarde en un diccionario.
# Después, debe mostrar por pantalla el mensaje ‘{nombre} tiene {edad} años y su número de teléfono es
# {teléfono}.

nombre = str(input("Agregue un nombre: "))
edad = int(input("Agregue un edad: "))
telefono = int(input("Agregue un teléfono: "))
datos = {"nombre": nombre, 'edad': edad, 'teléfono': telefono}

print(datos)

