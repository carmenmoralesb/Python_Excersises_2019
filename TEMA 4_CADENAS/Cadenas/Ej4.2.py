#!/usr/bin/env python
# -*- coding: utf-8 -*-

palabra = input("Mete una palabra : ")
palabracontada = ''
palabrarepe = ''

for letra in palabra:
    if letra not in palabrarepe:
        contador = palabra.count(letra)
        print(contador, " ", letra, end=" ")
        palabrarepe += letra

        # si letras no esta en palabra repe se concatena a palabrasrepe
        # y se concatena el valor de contador para cada letra
