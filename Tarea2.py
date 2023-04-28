'''
sueldo = float(input("Digite su salario: "))
valor_Ventas = float(input("Digite el valor de sus ventas: "))
sueldoT = round( sueldo + (valor_Ventas*0.1),  2)
print(f"\nTu sueldo total es= {sueldoT}")
'''
'''
valorP = float(input("Digite el precio del producto: "))
PrecioF = round(valorP*0.85, 2)
print(f"\nTendrá que pagar= {PrecioF}")
'''
'''
valor1 = float(input("Digite lo sacado en el primer examen: "))
valor2 = float(input("Digite lo sacado en el segundo examen: "))
valor3 = float(input("Digite lo sacado en el tercer examen: "))
calificacionF = round((valor1 + valor1 + valor1)/3, 2)
print(f"\nLa calificación final es= {calificacionF}")
'''
'''
valor1 = float(input("Digite la cantidad de hombres: "))
valor2 = float(input("Digite la cantidad de mujeres: "))
valorT = valor1+valor2
pHombres = valor1 / valorT
pMujeres = valor2 / valorT
print(f"\nEl porcentaje de hombres es= {(round(pHombres*100, 2))} %")
print(f"\nEl porcentaje de mujeres es= {(round(pMujeres*100, 2))} %")
'''