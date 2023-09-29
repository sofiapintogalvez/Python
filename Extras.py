if input("¿El carro no enciende?: ") == "no":
    print("Felicidades")
elif input("¿Tiene la llave conectada?: ") == "no":
    print("Conectar la llave")
elif input("¿La bateria tiene carga?: ") == "no":
    print("Llevar la bateria a cargar")
elif input("¿Los cables de la bateria estan buenos?: ") == "no":
    print("Reemplazarlos")
else:
    print("Llevar el auto a un tecnico")

n1 = float(input("#"))
n2 = float(input("#"))
n3 = float(input("#"))
n4 = float(input("#"))
n5 = float(input("#"))
n6 = float(input("#"))
n7 = float(input("#"))
n8 = float(input("#"))
n9 = float(input("#"))
m = [[n1,n2,n3] , [n4,n5,n6] , [n7,n8,n9]]
if m[0][0] == 1 == m[1][1] == m[2][2]:
    if m[0][1] == 0 == m[0][2] == m[1][0] == m[1][2] == m[2][0] == m[2][1]:
        print("Es matriz identidad")
    else:
        print("No es matriz identidad")
else:
    print("No es matriz identidad")

def matriz_real(lista):
    m = ""
    for x in range(len(lista)):
        for y in range(len(lista[x])):
            m += str(lista[x][y]) + "\t"
        m += "\n"
    return m
matriz = [[5,6,7],[2,3,4]]
print(matriz_real(matriz))

c = input("Ingrese una cadena: ")
cuenta = [0,0,0,0,0]
vocales = "aeiou"
for x in range(len(c)):
    if c[x] == "a":
        cuenta[0] = cuenta[0]+1
    elif c[x] == "e":
        cuenta[1] = cuenta[1]+1
    elif c[x] == "i":
        cuenta[2] = cuenta[2]+1
    elif c[x] == "o":
        cuenta[3] = cuenta[3]+1
    elif c[x] == "u":
        cuenta[4] = cuenta[4]+1
for x in range(len(cuenta)):
    print("Hay", cuenta[x], "ocurrencias de la vocal", vocales[x])

x = 1
sim = input("Ingrese simbolo: ")
sim2 = input("Ingrese simbolo: ")
n = int(input("Ingrese altura: "))
while x <= n:
    if x%2 == 1:
        print(sim*x)
        x+=1
    else:
        print(sim2*x)
        x+=1

lista = ["g.hola","p.hude","f.dew"]
usuario = ""
l = []
correo = "@ucsp.edu.pe"
for x in lista:
    usuario += x + correo
    l.append(usuario)
    usuario = ""
print(l)

lista = [[1,2,3],[24,35,67],[15,12,11],[76,89,210]]
nombres = ["costos farmacia","costos ropa","costos alimentos","costos ferreteria"]
suma = 0
total = 0
for x in range(len(lista)):
    for y in range(len(lista[x])):
        suma += lista[x][y]
        total += lista[x][y]
    print("El total de", nombres[x], "es:", suma)
    suma = 0
print("El total de la tienda es:", total)

def calcula_MCD(lista):
    if len(lista) == 0:
        return "lista vacía"
    if len(lista) == 1:
        return lista[0]
    
    menor = lista[0]
    for x in range(1,len(lista)):
        if lista[x] <= menor:
            menor = lista[x]

    l = []
    for x in range(len(lista)):
        if lista[x] != menor:
            mcd = lista[x]%menor
            l.append(mcd)
            
    mcd = l[0]
    for x in range(1,len(l)):
        if l[x] <= mcd:
            if l[x] > 0:
                mcd = l[x]
    return mcd

numeros = [40,50,20,8]
print(calcula_MCD(numeros))

def concatena_intercalado(a,b):
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a

    nueva = ""
    if len(a) > len(b) or len(a) == len(b):
        for x in range(len(a)):
            nueva += a[x]
            y = x
            for y in range(y,len(b)): 
                nueva += b[y]
                break
        return nueva
    else:
        for x in range(len(b)):
            nueva += b[x]
            y = x
            for y in range(y,len(a)):
                nueva += a[y]
                break
        return nueva

c1 = input("Ingrese cadena: ")
c2 = input("Ingrese cadena: ")
print(concatena_intercalado(c1,c2))

def corrige_email(lista):
  for x in lista:
    for y in range(len(x[1])):
      if x[1][y]=="@":
        break
    x[1] = x[1][:y]+"@ucsp.edu.pe"

datos = [["MARITZA LLANES","m.allanes@gmail.com"], ["OSVALDO ABARCA","o.abarca@hotmail.com"], ["ANA DIAZ ","a.diaz@vanguard.com"]]
corrige_email(datos)
print(datos)
