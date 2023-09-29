#Ejercicio 1: Crea una función, recibe parámetros de una cadena con mayúsculas y minúsculas, devuelve número de letras mayúsculas.
def cuenta_mayusculas(cadena):
    mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
    cantidad = 0
    for x in cadena:
        if x in mayusculas:
            cantidad += 1
    return cantidad

palabra = "SoFiA"
print("Hay", cuenta_mayusculas(palabra), "mayusculas en la palabra")

#Ejercicio 2: Crea una funcion que evalue una cadena ingresada por el usuario (sin espacios en blanco), retornar True o False si es palíndromo o no.
def es_palindromo(cadena):
    nc = ""
    i = 0
    for x in range(1,len(cadena)+1):
        nc += cadena[-x]
        if cadena[i] == nc[i]:
            rpta = "True"
        elif cadena[i] != nc[i]:
            rpta = "False"
            break
        i+=1
    return rpta

palabra = input("Ingrese palabra: ")
print(es_palindromo(palabra))

#Ejercicio 3: Crea una función, recibe parámetro dos cadenas: cadena y subcadena. Retornar True si la subcadena se encuentra dentro de cadena y False si no.
def encontrar_1(cadena,subcadena):
    if subcadena in cadena:
        return True
    return False

c1 = input("Ingrese cadena: ")
c2 = input("Ingrese subcadena: ")
print(encontrar_1(c1,c2))

#Ejercicio 4: Crea una funcion, recibe parametro cadena ingresada, retornar una nueva cadena siguiendo condiciones.
def tres_primeros_tres_ultimos(cadena):
    c1 = ""
    c2 = ""
    if len(cadena) >= 3:
        for x in range(3):
            c1 += cadena[x]
            c2 += cadena[-3+x]
        return c1 + c2
    elif len(cadena) < 3:
        return ""

c = input("Ingrese palabra: ")
print(tres_primeros_tres_ultimos(c))

#Ejercicio 5: Crea una funcion con cuatro parametros, los numeros son el segmento, se reemplaza en la lista 2.
def devuelve_segmento(inicio,fin,l1,l2):
    if inicio >= 0 and fin >= 0:
        if inicio < fin:
            if len(l2)-1 == fin:
                l1[inicio:fin+1] = l2[inicio:fin+1]
                return l1
            else:
                return l1
        else:
            return l1
    else:
        return l1

a = int(input("Ingrese inicio: "))
b = int(input("Ingrese fin: "))
lista1 = [1,2,3,4,5,6,7,8]
lista2 = [100,200,300,400,500]
print(devuelve_segmento(a,b,lista1,lista2))

#Ejercicio 6: Crea una función con parámetro lista anidada, retorna nueva lista con el número de elementos que hay en cada una de las sublistas.
def contador_lista(lista):
    l = []
    for x in range(len(lista)):
        for y in range(len(lista[x])):
            rpta = len(lista[x])
            break
        l += [rpta]
    return l

anidado = [[1,3], [5,7], [9,11], [13,15,17], [90,89,79,69]]
print(contador_lista(anidado))

#Ejercicio 7: Crea una función con parámetro lista anidada y entero, retorna nueva lista con el número de elementos mayores a n dentro de cada sublista.
def contador_lista_mayor_n(lista,n):
    rpta = 0
    l = []
    for x in range(len(lista)):
        for y in range(len(lista[x])):
            if lista[x][y] > n:
                rpta += 1
        l += [rpta]
        rpta = 0
    return l

anidado = [[1,3], [5,7], [9,11], [13,15,17], [90,89,79,69]]
numero = int(input("Ingrese numero: "))
print(contador_lista_mayor_n(anidado,numero))

#Ejercicio 8: Crea una funcion con argumento anidado y devuelve la lista invertida.
def invertir_lista(lista):
    l = []
    for x in range(1,len(lista)+1):
        l += [lista[-x]]
    return l

anidado = [[2,3,4,2,4], [0,2,4,5], [1,2,3,4]]
print(invertir_lista(anidado))

#Ejercicio 9: Crea funcion que retorne una nueva lista sin duplicados, no use in y not in.
def elimina_duplicados(lista):
    l = []
    l.append(lista[0])
    sumador = 0
    for x in range(len(lista)):
        for y in range(len(l)):
            if lista[x] != l[y]:
                sumador += 1
            if sumador == len(l):
                l.append(lista[x])
        sumador = 0
    return l

duplicado = [500,100,200,300,200,100,600,400,800,400,500,900]
print(elimina_duplicados(duplicado))

#Ejercicio 12: Crea una función con argumento n, crea una matriz con números de 1 a n x n.
def crear_matriz_hasta_n_x_n(n):
    matriz = []
    i = 1
    for x in range(n):
        m = []
        for y in range(n):
            if y < n:
                m.append(i)
                i+=1
        matriz.append(m)
    return matriz

num = int(input("Ingrese número: "))
print(crear_matriz_hasta_n_x_n(num))

#Ejercicio 13: Crea una función con cadena y subcadena, retorna posición de subcadena si esta dentro de cadena y -1 si no.
def encontrar_2(cadena,subcadena):
    contador = 0
    for x in range(len(cadena)-len(subcadena)+1):
        if cadena[x:len(subcadena)+x] == subcadena:
            return x
        else:
            contador += 1
        if contador == len(cadena)-len(subcadena)+1:
            return -1

c1 = input("Ingrese cadena: ")
c2 = input("Ingrese subcadena: ")
print(encontrar_2(c1,c2))

#Ejercicio 14: Crea función con parámetro lista M y valor n, extrae columna n de lista, verificar n en rango permitido. Caso contrario, retornar lista vacía.
def extrae_columna_n(lista,n):
    l = []
    if n < len(lista):
        for x in range(len(lista)):
            l.append(lista[x][n])
        return l
    else:
        return l
M = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
columna = int(input("Ingrese columna a extraer: "))
print(extrae_columna_n(M,columna))

#Ejercicio 17: Crea función con parámetro anidado y n, retorne anidado con indices de elementos de sublistas con longitud menor a n.
def cadenas_longitud_menor_n(n,lista):
    completa = []
    for x in range(len(lista)):
        l = []
        for y in range(len(lista[x])):
            if len(lista[x][y]) < n:
                l.append(y)
        completa.append(l)
    return completa

anidado = [['Mercurio','Venus','Tierra'], ['Marte','Jupiter','Saturno'], ['Urano','Neptuno']]
num = int(input("Ingrese numero: "))
print(cadenas_longitud_menor_n(num,anidado))

#Ejercicio 18: Crea función para imprimir listas anidadas (en forma matriz), no use índices.
def imprime_lista_anidada_1(lista):
    for x in lista:
        for y in x:
            print(y, end=" ")
        print()
        
anidado = [[1,2,3],[4,5],[6,7,8,9]]
imprime_lista_anidada_1(anidado)

#Ejercicio 19: Crea función para imprimir listas anidadas (en forma matriz), use índices.
def imprime_lista_anidada_2(lista):
    for x in range(len(lista)):
        for y in range(len(lista[x])):
            print(lista[x][y], end=" ")
        print()

anidado = [[1,2,3],[4,5],[6,7,8,9]]
imprime_lista_anidada_2(anidado)

#Ejercicio 20: Crea función que imprima el patrón "8", con parámetros ancho y alto, variable alto número entero impar, variable ancho número entero.
def patron(an,al):
    sim = "*"
    if 5 <= al <= 21 and 3 <= an <= 21:
        if al%2 != 0:
            for x in range(al):
                if x == 0 or x == ((al-1)/2) or x == (al-1):
                    for y in range(an):
                        print(sim, end="")
                    print()
                else:
                    print(sim, end=" "*(an-2))
                    print(sim)
        else:
            print("Altura no aceptada")
    else:
        print("Datos fuera de rango")

alto = int(input("Ingrese alto: "))
ancho = int(input("Ingrese ancho: "))
patron(ancho,alto)

#EXTRA: Modificar la misma lista.
def modificar_lista(indice,valor,lista):
    lista[indice] = valor
    
l = [1,2,3,4,5,6,7]
print("Modificar en la original:")
print(l)
modificar_lista(0,23,l)
print(l)

#EXTRA: Crear nueva lista y modificar.
def crear_lista(indice,valor,lista):
    lista[indice] = valor
    return lista

l = [1,2,3,4,5,6,7]
print("Crear nueva lista:")
print(l)
print(crear_lista(0,56,l[:]))
print(l)

