#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Factorial de un número entero

factorial=1
print ("Escribe un número")
Fac=int(input())
print ("El factorial de ese número es:")
for i in range (1,Fac+1):
	factorial=factorial*i
print factorial
