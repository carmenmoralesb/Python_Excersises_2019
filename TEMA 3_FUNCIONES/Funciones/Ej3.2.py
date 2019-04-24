#!/usr/bin/env python 
# -*- coding: utf-8 -*-

def areatriangulo(b,a):
   """Funcion que calcula el area de un triangulo dada su base y altura"""
   calculoarea = b*a/2
   return calculoarea

x = areatriangulo(5,6)
print("El area es " + str(x))