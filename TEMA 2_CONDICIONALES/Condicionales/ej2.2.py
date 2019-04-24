#!/usr/bin/python3
#Rehacer el programa del salario pero con control de errores
#meto dentro del try el bloque de codigo que se debe ejecutar si
#los datos que se dan son numeros 
try:
    horas_trabajo=int(input(("Escribe tus horas de trabajo:")))
    tarifa_horas=int(input(("Escribe el coste por horas:")))
    if horas_trabajo > 40:	
#calculo el extra
       extra = (1.5*tarifa_horas)*(horas_trabajo-40)
       total = (40*tarifa_horas) + extra
       #print("El salario extra " + str(extra))
       print("El salario es " + str(total))
    else:
       tarifa_normal=horas_trabajo*tarifa_horas 
       print("Tu salario es " + str(tarifa_normal))
#si no se ejecuta el except mostrando el error por pantalla
except:
	print("Error, por favor introduce un número")
