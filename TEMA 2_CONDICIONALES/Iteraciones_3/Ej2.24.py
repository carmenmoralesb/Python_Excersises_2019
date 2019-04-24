#!/usr/bin/env python
# -*- coding: utf-8 -*

diaactual=int(input("Introduce el dia actual: "))
mesactual=int(input("Introduce el mes actual: "))
añoactual=int(input("Introduce el año actual: "))

dianacimiento=int(input("Introduce tu dia de nacimiento: "))
mesnacimiento=int(input("Introduce tu mes de nacimiento: "))
añonacimiento=int(input("Introduce tu año de nacimiento: "))

if añoactual-añonacimiento < 20:
	print("Eres menor de 20")
elif añoactual - añonacimiento > 20:
	print("Eres mayor de 20")
else:
	if mesactual < mesnacimiento:
		print("Eres menor de 20")
	elif mesactual==mesnacimiento and dianacimiento<diaactual:
		print("Eres menor de 20")
	else:
		print("Eres mayor de 20")
