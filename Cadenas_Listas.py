#Ejercicio 3: Dada la variable mensaje, imprima el segmento del inicio a la coma.
mensaje = "Casi todas las cosas buenas que suceden en el mundo, nacen de una actitud de aprecio por los demás"
print(mensaje[:51])

#Ejercicio 4: Dada la variable mensaje, imprima el segmento de la ultima parte.
mensaje = "Casi todas las cosas buenas que suceden en el mundo, nacen de una actitud de aprecio por los demás"
print(mensaje[53:])

#Ejercicio 5: Dada la variable mensaje, imprima el segmento “todas nacen de una actitud de aprecio”.
mensaje = "Casi todas las cosas buenas que suceden en el mundo, nacen de una actitud de aprecio por los demás"
print((mensaje[5:10]) + " " + (mensaje[53:-14]))

#Ejercicio 6: Dada la variable mensaje, imprima el caracter que esta en la mitad.
mensaje = "Casi todas las cosas buenas que suceden en el mundo, nacen de una actitud de aprecio por los demás"
print(mensaje[int(len(mensaje)/2)])

#Ejercicio 7: Dada la variable mensaje, imprima “Casi todas las cosas lindas que suceden en la vida, se originan en una actitud de cariño por los demás”.
mensaje = "Casi todas las cosas buenas que suceden en el mundo, nacen de una actitud de aprecio por los demás"
print((mensaje[:20]) + " lindas " + (mensaje[28:42]) + " la vida, se originan en " + (mensaje[-36:-22]) + " cariño " + (mensaje[-13:]))

#Ejercicio 8: Dada la lista, elimine un índice dado por el usuario. Debe indicarle al usuario los límites de los índices.
lista = ["Hola", "Amigos", "Hoy", True]
print(lista)
indice = int(input("Ingrese el indice minimo a eliminar: "))
indice2 = int(input("Ingrese el indice maximo a eliminar: "))
lista[indice:indice2] = []
print(lista)

#Ejercicio 9: Dada la lista, pide al usuario una palabra y agregala al final e inicio de la lista.
lista = ["Hola", "Amigos", "Hoy", True]
palabra = input("Por favor ingrese una palabra: ")
lista[0:0] = [palabra]
lista.append(palabra)
print(lista)

#Ejercicio 10: Dada la lista, elimine el primer y último elemento de la lista.
lista = ["Hola", "Amigos", "Hoy", True]
lista[0:1] = []
lista[-1:4] = []
print(lista)

#Ejercicio 11: Dada la lista, cambie el True por False.
lista = ["Hola", "Amigos", "Hoy", True]
lista[3] = False
print(lista)

#Ejercicio 12: Dada la lista, pide al usuario nombre, apellido y edad, reemplazalos en los tres últimos valores.
lista = ["Hola", "Amigos", "Hoy", True]
nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = int(input("Por favor ingrese su edad: "))
lista[-3:] = [nombre, apellido, edad]
print(lista)

#Ejercicio 13: Dada la lista, pide al usuario nombre, apellido y edad, agregalos al inicio de la lista.
lista = ["Hola", "Amigos", "Hoy", True]
nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = int(input("Por favor ingrese su edad: "))
lista[0:0] = [nombre, apellido, edad]
print(lista)

#Ejercicio 14: Dada la lista, pide al usuario nombre, apellido y edad, reemplazalos al inicio de la lista.
lista = ["Hola", "Amigos", "Hoy", True]
nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = int(input("Por favor ingrese su edad: "))
lista[:3] = [nombre, apellido, edad]
print(lista)
