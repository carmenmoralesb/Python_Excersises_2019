mes = int(input("Escribe el mes "))
diacomienzomes = input("Dia en el que comienza el mes: L, M...")
dias = 0
contador=0

if mes == 1:
    mes = 'Enero'
    numdias = 31
elif mes == 2:
    mes = 'Febrero'
    numdias=28
elif mes == 3:
    mes = 'Marzo'
    numdias = 31
elif mes == 4:
    mes = 'Abril'
    numdias = 31
elif mes == 5:
    mes = 'Mayo'
    numdias = 31
elif mes == 6:
    mes = 'Junio'
    numdias = 31
elif mes == 7:
    mes = 'Julio'
    numdias = 31

elif mes == 8:
    mes = 'Agosto'
    numdias = 31

elif mes == 9:
    numdias = 31
    mes = 'Septiembre'

elif mes == 10:
    numdias = 31
    mes = 'Octubre'

elif mes == 11:
    numdias = 30
    mes = 'Noviembre'

elif mes == 12:
    numdias = 30
    mes = 'Diciembre'

if diacomienzomes == "L":
    d = 0
elif diacomienzomes == "M":
    d = 1
elif diacomienzomes == "X":
    d = 2
elif diacomienzomes == "J":
    d = 3
elif diacomienzomes == "V":
    d = 4
elif diacomienzomes == "S":
    d = 5
elif diacomienzomes == "D":
    d = 6

print('\n'+ mes +'\n')
print("L M X J V S D")

for dias in range(dias, numdias + d):
    dias += 1
    if dias <= d:
        print("  ", end="")
    if dias > d:
        contador += 1
        print('%d' % (contador) + " ", end="")
        if dias % 7 == 0 or d + contador == 7:
            print('\n')
