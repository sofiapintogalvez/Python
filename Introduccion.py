#Ejercicio 1: Escriba un programa que cree dos variables numéricas, calcule e imprima la suma.
x = 6
y = 8
suma = x+y
print(suma)

#Ejercicio 2: Escriba un programa que reciba dos números ingresados por teclado y calcule e imprima la suma.
x = float(input("Ingrese un número: "))
y = float(input("Ingrese un número: "))
suma = x+y
print(suma)

#Ejercicio 3: Escriba un programa que imprima en pantalla el siguiente patrón * ** *** ****
simbolo = "*"
print(simbolo + "\n" + simbolo * 2 + "\n" + simbolo * 3 + "\n" + simbolo * 4)

#Ejercicio 4: Escriba un programa que reciba un símbolo ingresado por teclado que imprima en pantalla el siguiente patrón + ++ +++ ++++
simbolo = input("Ingrese un símbolo: ")
print(simbolo + "\n" + simbolo * 2 + "\n" + simbolo * 3 + "\n" + simbolo * 4)

#Ejercicio 5: Escriba un programa que reciba un símbolo ingresado por teclado que imprima en pantalla el siguiente patrón +  + +  + + +  + + + +
sim = input("Ingrese un simbolo: ")
sim = sim + " "
print(sim + "\n" + sim * 2 + "\n" + sim * 3 + "\n" + sim * 4)

#Ejercicio 6: Escriba un programa que reciba dos símbolos ingresados por teclado, imprima el patrón.
sim = input("Ingrese un simbolo: ")
sim2 = input("Ingrese un simbolo: ")
print(sim * 22 + "\n"
      + sim * 9 , sim2 * 2 , sim * 9 + "\n"
      + sim * 8 , sim2 * 4 , sim * 8 + "\n"
      + sim * 7 , sim2 * 6 , sim * 7 + "\n"
      + sim * 6 , sim2 * 8 , sim * 6 + "\n"
      + sim * 5 , sim2 * 10 , sim * 5 + "\n"
      + sim * 4 , sim2 * 12 , sim * 4 + "\n"
      + sim * 3 , sim2 * 14 , sim * 3 + "\n"
      + sim * 2 , sim2 * 16 , sim * 2 + "\n"
      + sim , sim2 * 18 , sim + "\n"
      + sim * 22)

#Ejercicio 7: Escriba un programa que reciba por teclado dos números enteros positivos e imprima cociente y residuo de la división de ambos.
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
div1 = num1 // num2
div2 = num1 % num2
print("El cociente de la division de", num1, "y", num2, "es:", div1)
print("El residuo de la division de", num1, "y", num2, "es:", div2)

#Ejercicio 8: Escriba un programa que reciba por teclado dos números mayores que cero (flotantes) e imprima cociente, residuo y producto enteros.
num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese un numero: "))
div1 = int(num1 // num2)
div2 = int(num1 % num2)
prod = int(num1 * num2)
print("El cociente de la division de", num1, "y", num2, "es:", div1)
print("El residuo de la division de", num1, "y", num2, "es:", div2)
print("El producto de", num1, "y", num2, "es:", prod)
