#Ejercicio 1: Reciba un número n e imprima la tabla de multiplicar de n desde 1 hasta 100.
n = int(input("Ingrese un numero: "))
i = 1
while i <= 100:
    print(n, "x", i, "\t=\t", n*i)
    i+=1

n = int(input("Ingrese un numero: "))
for x in range(1,101):
    print(n, "x", x, "\t=\t", n*x)

#Ejercicio 2: Reciba 10 números enteros e imprima su valor promedio en la pantalla.
i = 1
suma = 0
while i <= 10:
    n = int(input("Ingrese un numero: "))
    suma += n
    i+=1
prom = suma/10
print("El promedio es: ", prom)

suma = 0
for x in range(10):
    n = int(input("Ingrese un numero: "))
    suma += n
print("El promedio es:", suma/10)

#Ejercicio 3: Reciba un número k e imprime todos los números del 0 a k que sean números impares.
k = int(input("Ingrese un numero: "))
i = 0
while i <= k:
    if i%2 != 0:
        print(i)
    i+=1

k = int(input("Ingrese un numero: "))
for x in range(k+1):
    if x%2 != 0:
        print(x)

#Ejercicio 4: Imprime la serie de Fibonacci entre 0 y 100 (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)
x = 0
y = 0
z = 0
while x <= 100:
    z = x+y
    print(x, end=" ")
    x = y
    y = z
    x+=1

#Ejercicio 6: Recibe un símbolo e imprima en pantalla el siguiente patrón + ++ ++++ ++++
sim = input("Ingrese un simbolo: ")
i = 1
while i == 1:
    while i <= 4:
        print(sim*i)
        i+=1
    i+=1

sim = input("Ingrese un simbolo: ")
for x in range(1):
    for x in range(1,5):
        print(sim*x)

#Ejercicio 7: Dada una lista y un símbolo, imprima los elementos de la lista con el símbolo como separador de los elementos.
sim = input("Ingrese un simbolo: ")
lista = [1,2,3,4]
i = 0
while i < len(lista):
    print(lista[i], end="")
    if i == len(lista)-1:
        break
    print(sim, end="")
    i+=1
print()

sim = input("Ingrese un simbolo: ")
lista = [1,2,3,4]
cadena = ""
i = 0
while i < len(lista):
    cadena+=str(lista[i])
    if i == len(lista)-1:
        break
    cadena += sim
    i+=1
print(cadena)

sim = input("Ingrese un simbolo: ")
lista = [1,2,3,4]
for x in range(len(lista)):
    print(lista[x], end="")
    if x == len(lista)-1:
        break
    print(sim, end="")
print()

#Ejercicio 8: Recibe cadenas las cuales se deben ir guardando en una lista, el programa debe parar cuando se marque la tecla q.
lista = []
while True:
    x = input("Ingrese una letra: ")
    if x != "q":
        lista.append(x) #lista += [x]
        print(lista)
    else:
        break

import itertools
lista = []
for x in itertools.count(1):
    cadena = input("Ingrese una letra: ")
    if cadena != "q":
        lista.append(cadena) #lista += x
        print(lista)
    else:
        break

#Ejercicio 9: Dada una lista de números, suma todos los elementos de dicha lista, la suma se debe guardar en una variable.
lista = [1,2,0,-1,10]
suma = 0
i = 0
while i < len(lista):
    suma += lista[i]
    i+=1
print("La suma de los elementos de la lista es:", suma)

lista = [1,2,0,-1,10]
suma = 0
for x in range(len(lista)):
    suma += lista[x]
print("La suma de los elementos de la lista es:", suma)

#Ejercicio 10: Dada una lista L, escribir un programa que cree una nueva lista sin los elementos duplicados. Utilice in y not in.
lista = [500,100,200,300,200,100,600,400,800,400,500,900]
l = []
i = 0
while i < len(lista):
    if lista[i] in l:
        del lista[i]
    else:
        l += [lista[i]]
    i+=1
print("La lista sin duplicados es:", l)

lista = [500,100,200,300,200,100,600,400,800,400,500,900]
l = []
for x in lista:
    if x in l:
        del x
    else:
        l += [x]
print("La lista sin duplicados es:", l)

#Ejercicio 11: Dada una lista de palabras, guarda en una variable la longitud de la palabra más larga.
lista = ["internacionalización","hola","como","estas","rocoto","mariposa"]
lon = len(lista[0])
i = 1
while i < len(lista):
    if lon > len(lista[i]):
        lon = lon
    else:
        lon = len(lista[i])
    i+=1
print("La longitud de la palabra mas larga es:", lon)

lista = ["internacionalización","hola","como","estas","rocoto","mariposa"]
lon = len(lista[0])
for x in range(1,len(lista)):
    if lon > len(lista[x]):
        lon = lon
    else:
        lon = len(lista[x])
print("La longitud de la palabra mas larga es:", lon)

#Ejercicio 12: Dada una lista de palabras, guarde en una variable el índice de la palabra más larga. Si no tiene nada, guarde -1.
lista = ["hola","como","estas","rocoto","mariposa","internacionalización"]
lon = len(lista[0])
ind = 0
i = 1
while i < len(lista):
    if lon > len(lista[i]):
        lon = lon
        ind = ind
    else:
        lon = len(lista[i])
        ind = i
    i+=1
print("El indice de la palabra mas larga es:", ind)

lista = ["hola","como","estas","rocoto","mariposa","internacionalización"]
lon = len(lista[0])
ind = 0
for x in range(1,len(lista)):
    if lon > len(lista[x]):
        lon = lon
        ind = ind
    else:
        lon = len(lista[x])
        ind = x
print("El indice de la palabra mas larga es:", ind)

#Ejercicio 13: Dada una cadena, crea una nueva donde se guarde la cadena invertida de la cadena original.
cadena = "hola"
nc = ""
i = 1
while i <= len(cadena):
    nc += cadena[-i]
    i+=1
print(nc)

cadena = "hola"
nc = ""
for x in range(1,len(cadena)+1):
    nc += cadena[-x]
print(nc)

#Ejercicio 14: Recibe dos cadenas, crea una nueva cadena formada por las dos cadenas dadas separadas por un espacio y sin vocales. 
c1 = input("Ingrese cadena: ")
c2 = input("Ingrese cadena: ")
c3 = ""
for i in range(2):
    for x in c1:
        if x != "a" and x != "e" and x != "i" and x != "o" and x != "u":
            c3+=x
    c3+=" "
    c1 = c2
print(c3)

#Ejercicio 1: Recibe un número entero positivo n e imprime el cálculo factorial de n.
n = int(input("Ingrese un numero: "))
fact = 1
i = 1
while i <= n:
    fact = fact*i
    i+=1
print("El factorial de dicho numero es:", fact)

n = int(input("Ingrese un numero: "))
fact = 1
for x in range(1,n+1):
    fact = fact*x
print("El factorial de dicho numero es:", fact)

#Ejercicio 2: Recibe dos números enteros x e y, imprima el cálculo del máximo común divisor.
n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))
mcd = 0
d = 1
while d <= n1 and d <= n2:
    if n1%d == 0 and n2%d == 0:
        mcd = d
        d+=1
    else:
        d+=1
print("MCD es:", mcd)

#Ejericio 3: Itere los números enteros del 1 al 100. Multiplos de tres imprima "Tres", múltiplos de cinco imprima "Cinco" y múltiplos ambos imprima "TresCinco".
i = 1
while i <= 100:
    if i%3 == 0 and i%5 == 0:
        print("TresCinco", end=" ")
    elif i%3 == 0:
        print("Tres", end=" ")
    elif i%5 == 0:
        print("Cinco", end=" ")
    else:
        print(i, end=" ")
    i+=1
print()

for x in range(1,101):
    if x%3 == 0 and x%5 == 0:
        print("TresCinco", end=" ")
    elif x%3 == 0:
        print("Tres", end=" ")
    elif x%5 == 0:
        print("Cinco", end=" ")
    else:
        print(x, end=" ")
print()

#Ejercicio 4: Recibe números enteros hasta que presione la tecla q y se debe imprimir el promedio de estos números.
suma = 0
lista = []
while True:
    n = input("Ingrese un numero: ")
    if n != "q":
        suma += int(n)
        lista += [n]
    else:
        break
print("El promedio de los numeros es:", suma/len(lista))

import itertools
suma = 0
lista = []
for x in itertools.count(1):
    n = input("Ingrese un numero: ")
    if n != "q":
        suma += int(n)
        lista += [n]
    else:
        break
print("El promedio de los numeros es:", suma/len(lista))

#Ejercicio 5: Recibe un símbolo y altura e imprima en pantalla el patrón.
sim = input("Ingrese un simbolo: ")
h = int(input("Ingrese la altura: "))
i = 1
while i <= h:
    print((h-i)*" " + sim*(i*2-1))
    i+=1

sim = input("Ingrese un simbolo: ")
h = int(input("Ingrese la altura: "))
for x in range(1,h+1):
    print((h-x)*" " + sim*(x*2-1))

#Ejercicio 6: Recibe dos símbolos y altura e imprima en pantalla el patrón.
sim = input("Ingrese un simbolo: ")
sim2 = input("Ingrese un simbolo: ")
h = int(input("Ingrese la altura: "))
i = 1
while i <= h:
    print((h-i)*" " + sim*(i*2-1))
    i+=1
j = 1
while j < h:
    print(j*" " + sim2*((h-j)*2-1))
    j+=1

sim = input("Ingrese un simbolo: ")
sim2 = input("Ingrese un simbolo: ")
h = int(input("Ingrese la altura: "))
for x in range(1,h+1):
    print((x-1)*" " + sim*((h-x)*2+1))
for x in range(1,h):
    print(x*" " + sim2*((h-x)*2-1))

#Ejercicio 1: Escribir un programa que imprima en pantalla el siguiente patrón.
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(i, end="")
        j+=1
    i+=1
    print()

for x in range(1,6):
    for y in range(1,x+1):
        print(x, end="")
    print()

#Ejercicio 3: Recibe un número e imprima el patrón, el tamaño de la base debe coincidir con el valor del número ingresado.
n = int(input("Ingrese un numero: "))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end="")
        j+=1
    i+=1
    print()

n = int(input("Ingrese un numero: "))
for x in range(1,n+1):
    for y in range(1,x+1):
        print(y, end="")
    print()

#Extra 1: Dada una lista, imprime cuantos elementos repetidos hay.
lista = [2,3,5,8,-1,3,8]
nl = []
for x in lista:
    if x in nl:
        continue
    else:
        nl += [x]
print("Hay", len(lista) - len(nl), "elementos repetidos")

#Extra 2: Pide una cadena e imprime True si es palindromo y False si no (se lee derecho y al reves).
cadena = input("Ingrese una palabra: ")
nc = ""
i = 0
for x in range(1,len(cadena)+1):
    nc += cadena[-x]
    if nc[i] == cadena[i]:
        rpta = "True"
    elif nc[i] != cadena[i]:
        rpta = "False"
        break
    i+=1
print(rpta)

