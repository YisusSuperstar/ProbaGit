#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Mediana de notas
Media=0
for i in range(1,11):
	print ("Dime tu nombre")
	Nomb=raw_input()
	print ("Dime tu nota")
	Not=int(input())
	Media=Media+Not
	
Medi=Media/10
print("Esta es la media de todas las notas:")
print Medi
print ("Y la persona con la nota más baja és:")
print 
