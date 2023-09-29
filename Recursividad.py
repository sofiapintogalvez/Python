#EJERCICIO CONTROL:
def concatena_cadenas_de_lista(l):
    if len(l) == 1:
        return l[0]
    else:
        if len(l) == 2 and concatena_cadenas_de_lista(l[1:]) == ".":
            return l[0] + concatena_cadenas_de_lista(l[1:])
        return l[0] + " " + concatena_cadenas_de_lista(l[1:])

print(concatena_cadenas_de_lista(["hola","amigo","somos","hermanos","."]))

#Ejercicio 1: Función que reciba entero mayor o igual que cero y devuelva el factorial de dicho número.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)

print(factorial(3))

#Ejercicio 2: Función que reciba entero n mayor o igual que 1 y devuelva el n-ésimo término de la serie.
def fibonacci(n):
    if n == 0 or n == 1 or n == 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(3))

#Ejercicio 3: Función que reciba cadena e imprima sus caracteres en una línea diferente.
def imprime_cadena(c):
    if len(c) == 1:
        print(c)
    else:
        print(c[0])
        imprime_cadena(c[1:])

imprime_cadena("toro")

#Ejercicio 4: Función que reciba entero n e imprima los números de n a 0 de forma descendente.
def imprime_descendente(n):
    if n >= 0:
        print(n)
        imprime_descendente(n-1)

imprime_descendente(5)

#Ejercicio 5: Función que reciba entero n e imprima los números de 0 a n de forma ascendente.
def imprime_ascendente(n,i):
    if i <= n:
        print(i)
        imprime_ascendente(n,i+1)

imprime_ascendente(5,0)

#Ejercicio 6: Función que reciba dos números y devuelva lista de n elementos con el valor de v.
def crea_lista(n,v):
    if n >= 1:
        return [v] + crea_lista(n-1,v)
    return []

print(crea_lista(4,2))

#Ejercicio 7: Función que reciba lista no vacìa de números y retorne la suma de esta lista.
def suma_lista(l):
    if len(l) == 1:
        return l[0]
    return l[0] + suma_lista(l[1:])
    
print(suma_lista([1,2,3,4]))

#Ejercicio 8: Función que reciba lista y retorna el mínimo elemento de la lista. 
def encuentra_minimo(l):
    if len(l) == 1:
        return l[0]
    return l[0] if l[0] < encuentra_minimo(l[1:]) else encuentra_minimo(l[1:])

print(encuentra_minimo([5,4,8,-1,0]))

#Ejercicio 9: Función que reciba altura y devuelva cadena con patrón triángulo.
def cadena_triangulo(a):
    if a == 1:
        return "*" + "\n"
    return cadena_triangulo(a-1) + "*"*a + "\n"

print(cadena_triangulo(5))

#Ejercicio 10: Función que reciba base y un exponente, devuelva el resultado.
def calcula_potencia(b,e):
    if e == 0:
        return 1
    if e == 1:
        return b
    return b*calcula_potencia(b,e-1)

print(calcula_potencia(-2,3))

#Ejercicio 11: Función que reciba cadena y retorna la cadena invertida.
def invertir_cadena(c,i):
    if i <= len(c):
        return c[-i] + invertir_cadena(c,i+1)
    return ""

print(invertir_cadena("hola",1))

#Ejercicio 12: Función que reciba cadena y diga True si es palindromo, False si no.
def es_palindromo(c):
    if len(c) == 1:
        return True
    else:
        if c[0] == c[-1]:
            return es_palindromo(c[1:-1])
        return False

print(es_palindromo("reconocer"))

#Ejercicio 2: Función que reciba lista y un número, modifique la lista con el valor de n.
def modifica_lista(l,n,i):
    if i < len(l):
        l[i] = n
        modifica_lista(l,n,i+1)
    l[0] = n

lista = [1,2,3,4]
modifica_lista(lista,5,0)
print(lista)

#Ejercicio 3: Función que reciba un número entero positivo y retorne la suma de sus dígitos.
def suma_digitos(n):
    if len(str(n)) == 1:
        return n
    n = str(n)
    return int(n[0]) + suma_digitos(int(n[1:]))

print(suma_digitos(12401))

#Ejercicio 4: Función que reciba una lista y número, retorne valor más cercano al número de la lista.
def menor(l):
    if len(l) == 1:
        return l[0]
    return l[0] if l[0] < menor(l[1:]) else menor(l[1:])

def cercano(lista,x):
    if len(lista) == 1:
        return lista[0]
    else:
        if x >= 0:
            return lista[0] if lista[0] > cercano(lista[1:],x) and lista[0] < x else cercano(lista[1:],x)
        else:
            return menor(lista)

print(cercano([8,5,1,11,4],-7))