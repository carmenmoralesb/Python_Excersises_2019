#!/usr/bin/python3
precio_producto=int( input("Escribe el importe final del producto : \n"))
#Primero evalua el tipo de IVA que el usuario ha metido en el programa y calcula tanto
#el impuesto que se ha aplicado como el precio final del producto

iva=(precio_producto*10)/100
precio_sin_iva=precio_producto-iva

print("Has pagado de más :" + str(iva) + " Euros")
print("El precio sin iva es " + str(precio_sin_iva) + " Euros")
