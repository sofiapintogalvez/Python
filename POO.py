#EJERCICIO CONTROL:
class Matriz:
    def __init__(self,f,c,lista):
        self.fil = f
        self.col = c
        self.m = []
        k = 0
        for i in range(f):
            y = []
            for j in range(c):
                y.append(lista[k])
                k += 1
            self.m.append(y)

    def __str__(self):        
        salida = ""
        for i in range(self.fil):
            for j in range(self.col):
                salida += str(self.m[i][j]) + "\t"
            salida = salida + "\n"
        return salida
    
    def intercambia_filas(self,i,j):
        nuevo = self.m[i]
        self.m[i] = self.m[j]
        self.m[j] = nuevo
        return self.m
    
    def __add__(self,otra_matriz):
        l = []
        for x in range(self.fil):
            for y in range(self.col):
                total = self.m[x][y] + otra_matriz.m[x][y]
                l.append(total)

        return Matriz(self.fil,self.col,l)

def main():
    m1 = Matriz(3,4,[1,2,3,4,5,6,7,8,9,-1,0,-2])
    print(m1)

    m2 = Matriz(3,4,[3,9,6,6,4,2,3,3,3,3,3,3])

    m1.intercambia_filas(1,2)
    print(m1)

    suma = m1 + m2
    print(suma)

main()


#Ejercicio 1: Clase punto y rectangulo, sobrecargar el str y lt; métodos area, perimetro, centro, punto a-b-c.
class punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,otro_punto):
        return punto(self.x + otro_punto.x, self.y + otro_punto.y)
    
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"
    
    def mostrar(self):
        print("(", self.x, ",", self.y, ")")

class rectangulo:
    def __init__(self,alto,ancho,inicio):
        self.alto = alto
        self.ancho = ancho
        self.p = inicio

    def mostrar(self):
        print("Alto =", self.alto)
        print("Ancho = ", self.ancho)
        print("Esquina =", end=" ")
        self.p.mostrar()

    def calcular_centro(self):
        return punto(self.p.x + self.ancho/2, self.p.y + self.alto/2)
    
    def calcular_area(self):
        return self.ancho * self.alto 
    
    def calcular_perimetro(self):
        return 2*(self.ancho + self.alto)
    
    def calcular_a(self):
        return punto(self.p.x, self.p.y + self.alto)
    
    def calcular_b(self):
        return punto(self.p.x + self.ancho, self.p.y + self.alto)
    
    def calcular_c(self):
        return punto(self.p.x + self.ancho, self.p.y)

    def __lt__(self,otro_rectangulo):
        return self.calcular_area() < otro_rectangulo.calcular_area()
        
def main():
    p1 = punto(2,3)
    p2 = punto(4,5)
    total = p1 + p2
    print("Suma de puntos:", total)
    
    print("PRIMER RECTANGULO")
    r = rectangulo(6,5,p1)
    r.mostrar()

    centro = r.calcular_centro()
    print("Punto Central =", end=" ")
    centro.mostrar()
    
    perimetro = r.calcular_perimetro()
    print("Perimetro =", perimetro)
    
    area = r.calcular_area()
    print("Area =", area)

    print("SEGUNDO RECTANGULO")
    r2 = rectangulo(6,7,p2)
    r2.mostrar()

    perimetro2 = r2.calcular_perimetro()
    print("Perimetro =", perimetro2)
    
    area2 = r2.calcular_area()
    print("Area =", area2)
    
    menor = area < area2
    print("¿El area de r es menor que el de r2?", menor)

    A = r.calcular_a()
    print("Punto A =", end=" ")
    A.mostrar()

    B = r.calcular_b()
    print("Punto B =", end=" ")
    B.mostrar()

    C = r.calcular_c()
    print("Punto C =", end=" ")
    C.mostrar()

main()

#Ejercicio 2: Clase potencia, atributos base y exponente, método calcular y mostrar.
class Potencia:
    def __init__(self,base,exponente):
        self.base = base
        self.exponente = exponente
    
    def calcular(self):
        return self.base**self.exponente
    
    def mostrar(self):
        print("Base =", self.base)
        print("Exponente =", self.exponente)

def main():
    p = Potencia(2,3)
    p.mostrar()
    c = p.calcular()
    print("El calculo es =", c)

main()