'''''
I. Diseña un programa en PYTHON para cada uno de los problemas
que se te plantean.
1. Se necesita un sistema que despliega una tabla de
multiplicar de un número dado por el usuario. ciclo for
2. Se necesita un sistema que pida un sueldo de un
trabajador, si el sueldo es mayor a 655000, no tedrá
ninguna bonificación, pero si es menor tiene bonificación
del 4%. Al final se desea saber el total del sueldo con
o sin bonificación. Preguntar si desea ejecutar de nuevo
el programa con el ciclo while.
3. Un maestro necesita un sistema para capturar las
calificaciones de 5 parciales de sus alumnos, después
recapturarlas necesita que se despliegue el promedio,
cuando ya no quiera capturar más alumnos, necesita que
se despliegue el promedio general de todos los alumnos
capturados. Preguntar si desea ejecutar de nuevo el
programa con el ciclo while.
4. Crear un bucle que cuente todos los números pares hasta
el 100 ciclo for
5. Haz una tabla de multiplicar utilizando el ciclo for
ciclo for
6. Escribir un programa que pregunte al usuario su edad y
muestre por pantalla todos los años que ha cumplido
(desde 1 hasta su edad). ciclo for
'''
'''
n = int(input("Digite el número que quiere para su tabla de multiplicar: "))
for i in range(0,11,1):
  print(str(i) + " * " + str(n) + " = " + str(i*n))

'''

'''
resp = "si"
while resp == "si" or resp == "s" or resp == "SI" or resp == "yes" or resp == "Si":  
    n = int(input("Digite el sueldo: "))
    #for i in range(0,11,1):
    if n > 655000:
        print("El empleado tendrá un sueldo total de = ${:,.0f}".format(n))
    elif n < 655000:
        print("El empleado tendrá un sueldo total de = ${:,.0f}".format((n*0.04)+n))
    resp = input("¿Desea calificar otro sueldo? ")

'''
''''
resp = "si"
resp2 = "si"
Alumnos = []
Contador = 0
Total = 0
while resp == "si" or resp == "s" or resp == "SI" or resp == "yes" or resp == "Si":
    while resp2 == "si" or resp2 == "s" or resp2 == "SI" or resp2 == "yes" or resp2 == "Si":  
        n1 = int(input("Digite el resultado del parcial 1: "))
        n2 = int(input("Digite el resultado del parcial 2: "))
        n3 = int(input("Digite el resultado del parcial 3: "))
        n4 = int(input("Digite el resultado del parcial 4: "))
        n5 = int(input("Digite el resultado del parcial 5: "))
        Total1 = round(((n1+n2+n3+n4+n5)/5),2) 
        Alumnos.append(Total1)
        resp2 = input("¿Desea añadir más alumnos? ")
    for numero in Alumnos:
        Contador = Contador + 1
        Total = Total + numero
    print(str(Total/Contador))
    resp = input("¿Desea ejecutar de nuevo el programa? ")
'''
'''
for numero in range(0, 101, 2):
    print(numero)
'''
'''
edad = int(input("Ingrese su edad: "))

for i in range(1, edad + 1):
    print("Ha cumplido", i, "años.")
'''

