#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Historico de edades

print ("Dime tu nombre")
Nomb=raw_input()
print ("Dime tu edad")
Ed=int(input())
print ("En que año estamos?")
An=int(input())
AnE=An-Ed
a=0
print("Tus edades en diferentes años:")
for i in range(AnE,An,1):
	a=i-AnE
	print "En",i,"tenias",a,"años"
print "Adios",Nomb
	

