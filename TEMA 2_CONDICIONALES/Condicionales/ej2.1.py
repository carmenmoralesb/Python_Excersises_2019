#!/usr/bin/python3
#Rehacer el programa del salario con salario extra
horas_trabajo=int(input(("Escribe tus horas de trabajo: ")))
tarifa_horas=int(input(("Escribe el coste por horas: ")))

#1.5 por cada hora extra
if horas_trabajo > 40:	
#calculo el extra
	extra = (1.5*tarifa_horas)*(horas_trabajo-40)
#las 40 horas siempre se cobran como tarifa normal
	total = (40*tarifa_horas) + extra
	print("El salario extra es " + str(extra))
	print("El salario es " + str(total))
else:
	tarifa_normal=horas_trabajo*tarifa_horas
	print("Tu salario es " + str(tarifa_normal))
