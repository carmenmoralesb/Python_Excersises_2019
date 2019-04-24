#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mcd(m,n):
    while m%n != 0:
        m_antes = m
        n_antes = n

        m = n_antes
        n = m_antes%n_antes
    return n

class Fraccion:
    def __init__(self,num,den=1):
        comun = mcd(num,den)
        self.num = num // comun
        self.den = den // comun
    
    def __str__(self):
        return "%d/%d" % (self.num,self.den)

# BINARIOS

    def __mul__(self,otro):
        if type(5) == type(otro):
           otro = Fraccion(otro) 
        nuevo_num = self.num * otro.num
        nuevo_den = self.den * otro.den
        return Fraccion(nuevo_num,nuevo_den)
    
    def __add__(self,otro):
        if type(5) == type(otro):
            otro = Fraccion(otro)
        
        nuevo_num = self.num*otro.den + self.den*otro.num
        nuevo_den = self.den * otro.den
        return Fraccion(nuevo_num,nuevo_den)

    __rad__ = __add__

    def __sub__(self,otro):
        if type(5) == type(otro):
            otro = Fraccion(otro)
        nuevo_num = self.num * otro.den - self.den * otro.num
        nuevo_den = self.den * otro.den
        return Fraccion(nuevo_num,nuevo_den)
    __rsub_ = __sub__    

    def __floordiv__(self,otro):
        if type(5) == type(otro):
            otro = Fraccion(otro)
        nuevo_num = self.num * otro.den
        nuevo_den = self.den * otro.num
        return Fraccion(nuevo_num,nuevo_den)
    __rfloor_ = __floordiv__    


    def __pow__(self,otro):
        if type(5) == type(otro):
            otro = Fraccion(otro)
        
        nuevo_num = self.num ** otro
        nuevo_den = self.den ** otro
        return Fraccion(nuevo_num,nuevo_den)
    __rpow_ = __pow__   

    def __truediv__(self,otro):
        if type(5) == type(otro):
            otro = Fraccion(otro)
        nuevo_num = self.num * otro.den
        nuevo_den = self.den / otro.num
        return Fraccion(nuevo_num,nuevo_den)
    __rtruediv_ = __truediv__    

# OPERACIONES EXTENDIDAS

    def __iadd__(self,otro):
        if type(5) == type(otro):
            otro = Fraccion(otro)
        nuevo_num = self.num * otro.den + self.den * otro.num
        nuevo_den = self.den * otro.den
        return Fraccion(nuevo_num,nuevo_den)
    __riadd_ = __iadd__    

    def __isub__(self,otro):
        if type(5) == type(otro):
            otro = Fraccion(otro)
        nuevo_num = self.num * otro.den - self.den * otro.num
        nuevo_den = self.den * otro.den
        return Fraccion(nuevo_num,nuevo_den)
    __risub_ = __isub__    

    def __imul__(self,otro):
        if type(5) == type(otro):
            otro = Fraccion(otro)
        nuevo_num = (self.num * otro.den) * (self.den * otro.num)
        nuevo_den = self.den * otro.den
        return Fraccion(nuevo_num,nuevo_den)
    __rmul__ = __imul__    

    def __idiv__(self,otro):
        if type(5) == type(otro):
            otro = Fraccion(otro)

        nuevo_num = (self.num * otro.den) / (self.den * otro.num)
        nuevo_den = self.den * otro.den
        return Fraccion(nuevo_num,nuevo_den)
    __rdiv__ = __idiv__    

    def __ifloordiv__(self,otro):
        if type(5) == type(otro):
            otro = Fraccion(otro)
        nuevo_num = (self.num * otro.den) // (self.den * otro.num)
        nuevo_den = self.den * otro.den
        return Fraccion(nuevo_num,nuevo_den)
    __rifloor__ = __ifloordiv__    


    def __ipow__(self,otro):
        if type(5) == type(otro):
            otro = Fraccion(otro)
        nuevo_num = (self.num ** otro.den) ** (self.den ** otro.num)
        nuevo_den = self.den ** otro.den
        return Fraccion(nuevo_num,nuevo_den)
    __ripow__ = __ipow__    


# OPERADORES UNARIOS

    def __neg__(self):
        return Fraccion(-self.num,self.den)
    
    def __pos__(self):
        return Fraccion(self.num,self.den)
    
    def __abs__(self):
        return Fraccion(abs(self.num),self.den)

    def __invert__(self):
        return Fraccion(self.den,self.num)

    def __int__(self):
        return int(self.num//self.den) 
    
    #def __long__(self):
    #    return long(self.den,self.num) No hay long en python3!!!!
    
    def __float__(self):
        return float(self.den/self.num)  


# OPERACIONES DE COMPARACIÓN

    def __eq__(self,otro):
       if not (self.num * self.den) - (otro.num * otro.den):return True
       return False

    def __ne__(self,otro):
        if (self.num * self.den) - (otro.num * otro.den):return True
        return False

    def __gt__(self,otro):
        if (self.num * self.den) - (otro.num * otro.den) > 1: return True  
        return False

    def __lt__(self,otro):
        if (self.num * self.den) - (otro.num * otro.den) < 0: return True
        return False

    def __le__(self,otro):
        if (self.num * self.den) - (otro.num * otro.den) < 0 or (self.num * self.den) - (otro.num * otro.den) == 0 : return True
        return False
    
    def __ge__(self,otro):
        if (self.num * self.den) - (otro.num * otro.den) > 0 or (self.num * self.den) - (otro.num * otro.den) == 0 :return True
        return False 


# PRUEBAS

f1 = Fraccion(4,3)
f2 = Fraccion(1,2)

suma = f1 + f2
print("La suma es " + "%s" %(suma))

resta = f1 - f2
print("La resta es " + "%s" %(resta))

multiplicacion = f1 * f2
print("La multiplicación es " + "%s" %(multiplicacion))

divisioncompleta = f1 // f2
print("La división exacta es " + "%s" %(divisioncompleta))

divisionincomp = f1 / f2
print("La división inexacta es " + "%s" %(divisionincomp))

subs = f1 - f2
print("La resta es " + "%s" %(subs))

exponencial = f1 ** 0.5
print("El exponencial es " + "%s" %(exponencial))

f1 += f2 
print("El sumatorio es " + "%s" %(f1))

f1 = Fraccion(4,3)
f2 = Fraccion(1,2)

f1 -= f2
print("La subtracción es " + "%s" %(f1))

f1 = Fraccion(4,3)
f2 = Fraccion(1,2)

f1 *= f2
print("La multiplicación extendida es " + "%s" %(f1))

f1 = Fraccion(4,3)
f2 = Fraccion(1,2)

f1 /= f2
print("La división extendida no entera es " + "%s" %(f1))

f1 = Fraccion(4,3)
f2 = Fraccion(1,2)

f1 //= f2
print("La división extendida entera es " + "%s" %(f1))

f1 = Fraccion(4,3)
f2 = Fraccion(1,2)

f1 **= f2
print("El exponente añadido es " + "%s" %(f1))

f1 = Fraccion(4,3)
f2 = Fraccion(1,2)


print("Es igual " + str(f1) + " que " + str(f2) + ": " + str(f1 == f2))

print("Es distinto " + str(f1) + " que " + str(f2) + ": " + str(f1 != f2))

print("Es mayor " + str(f1) + " que " + str(f2) + ": " + str(f1 > f2))

print("Es menor " + str(f1) + " que " + str(f2) + ": " + str(f1 < f2))

print("Es mayor o igual " + str(f1) + " que " + str(f2) + ": " + str(f1 >= f2))

print("Es menor o igual " + str(f1) + " que " + str(f2) + ": " + str(f1 <= f2))

