'''''
#No de Identificación, Nombres, Apellidos, Dirección, Teléfono, Edad, Estado Civil, Número de hijos, Estatura en centímetros, fecha de contratación (Día/mes/año), Sueldo básico, Días Laborados.

Taller 2:

Dando continuidad con la primera entrega del proyecto, en esta oportunidad el estudiante debe realizar las siguientes validaciones utilizando la sentencia condicional IF.

Si el empleado es mayor de 55 años disfrutará de un bono de prepensión correspondiente al 5% de su sueldo básico.

Si el empleado es casado y tiene hijos se le otorgará un paseo cada diciembre

Si el sueldo básico está entre 1000000 y 1500000 tendrá una comisión del 2% sobre el valor del sueldo; Si el sueldo básico está entre 1500001 y 2000000 tendrá una comisión del 5% sobre el valor del sueldo; para todos los demás casos no habrá comisión.

Si el empleado trabajó más de 20 días al mes y su sueldo es menor a 1000000 tendrá derecho a un bono de alimentación.
'''
def calcular():
  if edad > 55:
    print("El empleado tendrá un bono de prepensión por valor de = ${:,.0f}".format((sueldo*0.05)))
  else:
    print("El empleado no tendrá bono de prepensión")

  if estado_civil == "Casado" and hijos > 0:
    print("El empleado tendrá derecho a un paseo cada diciembre")
  else:
    print("El empleado no tendrá derecho a un paseo cada diciembre")

  if sueldo >= 1000000 and sueldo <= 1500000:
    print("El empleado tendrá una comisión por valor de = ${:,.0f}".format((sueldo*0.02)))
  elif sueldo >= 1500001 and sueldo <= 2000000:
    print("El empleado tendrá una comisión por valor de = ${:,.0f}".format((sueldo*0.05)))
  else:
    print("El empleado no tendra bono por comisión")

  if diasLabMes > 20 and sueldo < 1000000:
    print("El empleado tiene derecho a un bono de alimentación")
  else:
    print("El empleado no tiene derecho a un bono de alimentación")

resp = "Si"
while resp == "si" or resp == "s" or resp == "SI" or resp == "yes" or resp == "Si":
  identificación = 1023658847
  nombres = "Pepito Juliano"
  apellidos = "Suarez Mendieta"
  dirección = "Cra 21 #20-03"
  teléfono = 3105627984
  edad = 31
  estado_civil = "Soltero"
  hijos = 0
  estatura_cm = 183
  f_contratación = "11/05/2021"
  sueldo = 900000
  diasLab = "489"
  diasLabMes = 21
  calcular()
  
  resp = input("¿Desea ejecutar de nuevo el programa? ")




