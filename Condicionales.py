#Ejercicio 1: Escriba un programa que reciba valores enteros de largo y ancho e imprima si es cuadrado o no.
largo = int(input("Ingrese el largo: "))
ancho = int(input("Ingrese el ancho: "))
if largo == ancho:
    print("La figura es un cuadrado")
else:
    print("La figura no es un cuadrado")

#Ejercicio 2: Escriba un programa que reciba dos números y un operador matemático(+,-,*,/). Haz la operación e imprime el resultado. Si es otro operador no lo aceptes.
num = float(input("Ingrese un número: "))
num2 = float(input("Ingrese un número: "))
operador = input("Ingrese el operador: ")
if operador == "+":
    print("La suma es:", num + num2)
elif operador == "-":
    print("La resta es:", num - num2)
elif operador == "*":
    print("La multiplicación es:", num * num2)
elif operador == "/":
    print("La división es:", num / num2)
else:
    print("Operador no aceptado")

#Ejercicio 3: Una empresa da bonificación del 5% si trabajó más de 3 años. Pide el salario y los años de servicio e imprima la cantidad neta de la bonificación.
salario = float(input("Ingrese su salario: "))
if int(input("Ingrese los años de trabajo: ")) > 3:
    bono = (0.05 * salario) + salario
    print("Su bono es:", bono)
else:
    print("No cumple los requisitos para la bonificación")

#Ejercicio 4: Teniendo en cuenta que la nota por debajo de 60 es C, entre 60 y 80 es B, más de 80 es A. Recibe la nota e imprima la calificación.
nota = float(input("Ingrese su nota: "))
if nota < 60:
    print("Tu calificación es C")
elif 60 <= nota <= 80:
    print("Tu calificación es B")
elif nota > 80:
    print("Tu calificación es A")
else:
    print("No tienes calificación")

#Ejercicio 2: Escribe un programa que reciba la edad de 3 personas y determinar la edad del más joven entre ellos.
e1 = int(input("Ingrese su edad: "))
e2 = int(input("Ingrese su edad: "))
e3 = int(input("Ingrese su edad: "))
if e1 < e2 and e1 < e3:
    print("El más joven es:", e1)
elif e2 < e1 and e2 < e3:
    print("El más joven es:", e2)
elif e3 < e1 and e3 < e2:
    print("El más joven es:", e3)
else:
    print("Todos tienen la misma edad")

#Ejercicio 3: Reciba tres lados(cm) de un triángulo y diga si es equilátero, isósceles o escaleno.
l1 = float(input("Ingrese un lado: "))
l2 = float(input("Ingrese un lado: "))
l3 = float(input("Ingrese un lado: "))
if l1 == l2 and l1 == l3 and l2 == l3:
    print("Es un triangulo equilatero")
elif l1 != l2 and l1 != l3 and l2 != l3:
    print("Es un triangulo escaleno")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("Es un triangulo isoseles")

#Ejercicio 4: Recibe por teclado la edad, el estado civil soltero/a o casado/a. Imprima el lugar a trabajar.
edad = int(input("Ingrese su edad: "))
estado = input("Ingrese su estado civil (S o C): ")
if estado == "C":
    print("Usted trabajará sólo en zonas urbanas")
elif estado == "S" and 20 <= edad <= 50:
    print("Usted puede trabajar en cualquier lugar")
elif estado == "S" and 50 < edad <= 70:
    print("Usted trabajará sólo en áreas urbanas")
else:
    print("ERROR")

#Ejercicio 5: Recibe el número de clases impartidas y clases asistidas, imprime si es apto o no de dar el examen.
impartidas = int(input("Ingrese la cantidad de clases impartidas: "))
asistidas = int(input("Ingrese la cantidad de clases asistidas: "))
p = (asistidas / impartidas) * 100
if p < 70:
    causa = input("Ingrese si tiene causa medica (S o N): ")
    if causa == "S":
        print("Es apto para dar el examen")
    elif causa == "N":
        print("No es apto para dar el examen")
else:
    print("Es apto para dar el examen")

#Ejercicio 6: De la lista, recibe un valor que diga True si el trimestral supero al valor, caso contrario False.
lista = ["Marzo", 10000, "Enero", 20000, "Febrero", 21000]
dato = float(input("Ingrese un numero: "))
total = lista[1] + lista[3] + lista[5]
if dato < total:
    lista.append(True)
else:
    lista.append(False)
print(lista)

#Ejercicio 7:  De la lista, reciba un valor que diga True si al menos en un mes es el valor dado, sino False.
lista = ["Marzo", 10000, "Enero", 20000, "Febrero", 21000]
dato = float(input("Ingrese un numero: "))
if dato == lista[1] or dato == lista[3] or dato == lista[5]:
    lista.append(True)
else:
    lista.append(False)
print(lista)

#Ejercicio 8: Escribe un programa para comprobar si un año es bisiesto o no.
anio = int(input("Ingrese el año: "))
if anio%4 == 0:
    if anio%100 == 0:
        if anio%400 == 0:
            print("Es año bisiesto")
        else:
            print("No es año bisiesto")
    else:
        print("Es año bisiesto")
else:
    print("No es año bisiesto")

#Ejercicio 9: Dada la lista escriba un programa que imprima si el nombre se encuentra en la lista o no.
l = ["Hugo", "Martin", "Lucas", "Mateo", "Leo", "Daniel", "Alejandro", "Pablo"]
nom = input("Ingrese su nombre: ")
if nom == l[0] or nom == l[1] or nom == l[2] or nom == l[3] or nom == l[4] or nom == l[5] or nom == l[6] or nom == l[7]:
    print(nom, "se encuentra en la lista")
else:
    print(nom, "no se encuentra en la lista")

#Ejercicio 10: Pide al usuario un número entre 1 y 7 que es día de la semana, el dia en numero y un número entre 1 y 12 que es mes del año, imprima la fecha.
dia = int(input("Ingrese un numero entre el 1 y 7: "))
num = int(input("Ingrese el numero de dia: "))
mes = int(input("Ingrese un numero entre el 1 y 12: "))
if 1 <= dia <= 7 and 1 <= mes <= 12 and 1 <= num <= 31:
    d = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
    m = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    print("Hoy es", d[dia-1], num, "de", m[mes-1])
else:
    print("Los datos ingresados no existen")
