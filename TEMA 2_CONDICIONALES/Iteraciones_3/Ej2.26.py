#!/usr/bin/env python 

#Dada la siguiente serie: a1=0, a2=1, an=3*an-1+2*an-2 (para n>=3)
#Calcular el valor y el rango (la n) del primer término mayor o igual a 1000.

contador = 2 #ya conocemos asub2 y asub2
actual = 1
anterior = 0
a = 0

while a <= 1000:
    a = 3*(actual) + 2*(anterior)
    anterior = actual
    actual = a
    contador+=1
print("El rango es: " + str(contador))
print("El primer numero mayor o igual que 1000 es " + str(a))
