#EJERCICIO CONTROL:
class Agenda:
    def __init__(self,p_d,f_p):
        self.p_d = p_d
        self.f_p = f_p

class Persona:
    def __init__(self,p_n,s_n,a_p,a_m,h_t,edad):
        self.p_n = p_n
        self.s_n = s_n
        self.a_p = a_p
        self.a_m = a_m
        self.h_t = h_t
        self.edad = edad

    def __le__(self,otra_persona):
        return self.h_t <= otra_persona.h_t

    def nombre_completo(self,orden):
        if orden == "apellido":
            return self.a_p + " " + self.a_m + " " + self.p_n + " " + self.s_n
        elif orden == "nombre":
            return self.p_n + " " + self.s_n + " " + self.a_m + " " + self.a_p
        else:
            return "No existe"

class CEO(Persona):
    def __init__(self,p_n,s_n,a_p,a_m,h_t,edad,agen):
        super().__init__(p_n,s_n,a_p,a_m,h_t,edad)
        self.agen = agen

class Administrativo(Persona):
    def __init__(self,p_n,s_n,a_p,a_m,h_t,edad,area):
        super().__init__(p_n,s_n,a_p,a_m,h_t,edad)
        self.area = area

class Personal_limpieza(Persona):
    def __init__(self,p_n,s_n,a_p,a_m,h_t,edad,c_o_a,c_o_l):
        super().__init__(p_n,s_n,a_p,a_m,h_t,edad)
        self.c_o_a = c_o_a
        self.c_o_l = c_o_l

def main():
    agen = Agenda("Peru","15/05/22")
    ceo = CEO("Sofía","Alejandra","Pinto","Gálvez",14,19,agen)
    admin = Administrativo("Ernesto","Jesus","Gonzales","Casas",45,67,"R.R.H.H.")
    
    x = ceo <= admin
    print(x)
    y = admin.nombre_completo("apellido")
    print(y)

main()

#Ejercicio 1: Clase Auto, constructor atributos color, matrícula, destino. Clase Auto hereda de Transporte atributos velocidad, capacidad.
class Transporte:
    def __init__(self,velocidad,capacidad):
        self.velocidad = velocidad
        self.capacidad = capacidad

    def __str__(self):
        return "El auto tiene una velocidad de " + str(self.velocidad) + "km/h" + ", capacidad de " + str(self.capacidad)

class Auto(Transporte):
    def __init__(self,velocidad,capacidad,color,matricula,destino):
        super().__init__(velocidad,capacidad)
        self.color = color
        self.matricula = matricula
        self.destino = destino

    def __str__(self):
        return super().__str__() + ", el color es " + self.color + ", la matricula es " + str(self.matricula) + " y su destino es " + self.destino

def main():
    a = Auto(123,4,"rojo","V4Y-680","Rusia")
    print(a)

main()

#Ejercicio 2: Dos subclases Ave y Perro que hereden de la clase Animal. Atributos y métodos en la imagen.
class Animal:
    def __init__(self,color,peso):
        self.color = color
        self.peso = peso

    def Comer(self):
        return "comiendo"

    def Moverse(self):
        return "moviendose"

class Ave(Animal):
    def __init__(self,color,peso,tipo):
        super().__init__(color,peso)
        self.tipo = tipo

    def Volar(self):
        return "volando"

class Perro(Animal):
    def __init__(self,color,peso,raza):
        super().__init__(color,peso)
        self.raza = raza

    def Ladrar(self):
        return "ladrando"

def main():
    a = Ave("azul",23,"Paloma")
    p = Perro("marron",12,"Chihuaha")
    
    c = a.Comer()
    print(c)
    v = a.Volar()
    print(v)
        
main()

#Ejercicio 3: Clase hija hereda de madre que hereda de abuela.
class Abuela:
    def __init__(self,color_ojos,cabello):
        self.color_ojos = color_ojos
        self.cabello = cabello
        
class Madre(Abuela):
    def __init__(self,color_ojos,cabello,altura,contextura_fisica):
        super().__init__(color_ojos,cabello)
        self.altura = altura
        self.contextura_fisica = contextura_fisica
        
class Hija(Madre):
    def __init__(self,color_ojos,cabello,altura,contextura_fisica,nombre,edad):
        super().__init__(color_ojos,cabello,altura,contextura_fisica)
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Mi nombre es " + self.nombre + ", tengo " + str(self.edad) + " años. Mi madre mide " + str(self.altura) + " y su contextura es " + self.contextura_fisica + ". Mi abuela tiene los ojos color " + self.color_ojos + " y el cabello " + self.cabello

def main():
    h = Hija("marrones","negro",157,"media","Amelia",23)
    print(h)

main()

#Ejercicio 4: Clase docente y administrador que heredan de persona.
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Nombre = " + self.nombre + ", Edad = " + str(self.edad)

class Docente(Persona):
    def __init__(self,nombre,edad,cargo,horas_trabajadas):
        super().__init__(nombre,edad)
        self.cargo = cargo
        self.horas_trabajadas = horas_trabajadas

    def __str__(self):
        return super().__str__() + ", Cargo = " + self.cargo + ", Horas trabajadas = " + str(self.horas_trabajadas)

class Administrador(Persona):
    def __init__(self,nombre,edad,area):
        super().__init__(nombre,edad)
        self.area = area

    def __str__(self):
        return super().__str__() + ", Area = " + self.area

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado,nota):
        super().__init__(nombre,edad)
        self.grado = grado
        self.nota = nota

    def __str__(self):
        return super().__str__() + ", Grado = " + str(self.grado) + ", Nota = " + str(self.nota)

def main():
    e = Estudiante("Alex",15,5,20)
    a = Administrador("Rogers",34,"Recursos Humanos")
    d = Docente("Marcela",42,"Prof. Matematicas",87)

    print("ESTUDIANTE", "\n", e, "\n")
    print("ADMINISTRADOR", "\n", a, "\n")
    print("DOCENTE", "\n", d, "\n")

main()

#Ejercicio 6: Clase figura; circulo y cuadrilatero heredan de ella, cuadrado y rombo heredan de los anteriores.
import math

class Figura:
    def __init__(self,color):
        self.color = color
    
    def __str__(self):
        return "Color = " + self.color

class Circulo(Figura):
    def __init__(self,color,radio):
        super().__init__(color)
        self.radio = radio
    
    def area(self):
        return math.pi*(math.pow(self.radio,2))
    
    def perimetro(self):
        return math.pi*(self.radio*2)
    
    def __str__(self):
        return super().__str__() + "Radio = " + self.radio + self.area() + self.perimetro()

class Cuadrilatero(Figura):
    def __init__(self,color,lado):
        super().__init__(color)
        self.lado = lado
    
    def perimetro(self):
        return self.lado*4
    
    def __str__(self):
        return super().__str__() + "Perimetro = " + self.perimetro()

class Cuadrado(Cuadrilatero):
    def __init__(self,color,lado):
        super().__init__(color,lado)
    
    def area(self):
        return math.pow(self.lado,2)
    
    def __str__(self):
        return super().__str__() + "Area cuadrado = " + self.area()

class Rombo(Cuadrilatero):
    def __init__(self,color,lado,diagonal_mayor,diagonal_menor):
        super().__init__(color,lado)
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor
    
    def area(self):
        return (self.diagonal_mayor*self.diagonal_menor)/2
    
    def __str__(self):
        return super().__str__() + "Area rombo = " + self.area()

def main():
    c = Cuadrado("verde",5)
    r = Rombo("rojo",3,8,4)
    cr = Circulo("azul",6)

    ac = c.area()
    print("Area cuadrado =", ac)
    pc = c.perimetro()
    print("Perimetro cuadrado =", pc)

    ar = r.area()
    print("Area rombo =", ar)
    pr = r.perimetro()
    print("Perimetro rombo =", pr)

    acr = cr.area()
    print("Area circulo =", acr)
    pcr = cr.perimetro()
    print("Perimetro circulo =", pcr)

main()