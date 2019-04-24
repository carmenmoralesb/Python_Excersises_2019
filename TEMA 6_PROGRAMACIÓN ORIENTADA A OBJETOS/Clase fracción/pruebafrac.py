#!/usr/bin/env python
# -*- coding: utf-8 -*-

f1 = 4/3
f2 = 1/2

suma = f1 + f2
resta = f1 - f2
multi = f1 * f2
diviex = f1 / f2
divinoex = f1 // f2
power = f1 ** 0.5

print("[Suma] " + str(suma))
print("[Resta] " + str(resta))
print("[Multiplicación] " + str(multi))
print("[División] " + str(diviex))
print("[Division entera] " + str(divinoex))

f1 += f2
print("Adición")
print(f1)

f1 = 4/3
f2 = 1/2

f1 -= f2
print("Substrac")
print(f1)

f1 = 4/3
f2 = 1/2

f1 *= f2

print("Exponen")
print(f1)

f1 = 4/3
f2 = 1/2

f1 /= f2
print("iDiv")
print(f1)

f1 = 4/3
f2 = 1/2

f1 //= f2
print("iFloorDiv")
print(f1)

f1 = 4/3
f2 = 1/2

f1 **= f2

print("[iPower] ")
print(f1)