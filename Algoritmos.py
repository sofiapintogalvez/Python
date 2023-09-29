#Algoritmo de Ordenamiento por selección
def ordenamiento_seleccion(l):
    for x in range(len(l)):
        minimo = x
        for y in range(x,len(l)):
            if l[y] < l[minimo]:
                minimo = y
        if minimo != x:
            aux = l[x]
            l[x] = l[minimo]
            l[minimo] = aux
    return l

lista = [7,9,2,4,3,1,8,0]
print(ordenamiento_seleccion(lista))

#Algoritmo de Búsqueda Binaria
def busqueda_binaria(l,v):
    pasos = 0
    izq = 0
    der = len(l)-1
    while izq <= der:
        pasos+=1
        centro = (izq+der)//2
        if l[centro] == v:
            print("Valor encontrado en", pasos, "pasos en la posicion", centro)
            break
        elif l[centro] > v:
            der = centro-1
        elif l[centro] < v:
            izq = centro+1
        else:
            print("Elemento no encontrado")

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
valor = int(input("Ingrese valor a buscar: "))
busqueda_binaria(lista,valor)

#Algortimo de ordenamiento por inserción
def ordenamiento_insercion(l):
    for x in range(1,len(l)):
        actual = l[x]
        indice = x
        while indice > 0 and l[indice-1] > actual:
            l[indice] = l[indice-1]
            indice -= 1
        l[indice] = actual
    return l

lista = [5,3,1,4,2,6]
print(ordenamiento_insercion(lista))

#Algoritmo de ordenamiento burbuja
def ordenamiento_burbuja(l):
    for x in range(1,len(l)):
        for y in range(len(l)-x):
            if l[y] > l[y+1]:
                aux = l[y]
                l[y] = l[y+1]
                l[y+1] = aux
    return l

lista = [6,5,3,1,8,7,2,4]
print(ordenamiento_burbuja(lista))