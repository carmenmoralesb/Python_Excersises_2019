#!/usr/bin/python3
"""valoresmetidos = 0
#numero de valores q has metido
totalsuma = 0
#total antes de empezar a sumar
#mientras q el numero de datos sea menor q tres pedira numeros y se iran añadiendo sus valores al total
while valoresmetidos < 3:
    valoresmetidos += 1  #en cada iteracion sumo uno
    totalsuma += int(input("Escribe los números que quiere sumar: ")) #al total le voy sumando las entradas
print ("La suma de todos los números es: " + str(totalsuma))"""

#otraforma

a = int(input("Escribe los números que quiere sumar: "))
b = int(input("Escribe los números que quiere sumar: "))

print(a + b + int(input("Escribe los números que quiere sumar: ")))