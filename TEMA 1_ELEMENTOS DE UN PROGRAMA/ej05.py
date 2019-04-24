#!/usr/bin/python3
precio_producto=int( input("Escribe el precio del producto : \n"))
iva_producto=int( input("El tipo de producto que has comprado: \n 1: 4% \n 2: 10% \n 3:21% \n"))
#Primero evalua el tipo de IVA que el usuario ha metido en el programa y calcula tanto
#el impuesto que se ha aplicado como el precio final del producto

if iva_producto==1:
   iva=4
elif iva_producto==2:
   iva=10
elif iva_producto==3:
   iva=21

iva=(precio_producto*iva/100)
precio_final=(precio_producto*iva/100 + precio_producto)  

print("Has pagado de más :" + str(iva) + " Euros")
print("El precio final que has pagado es " + str(precio_final) + " Euros")