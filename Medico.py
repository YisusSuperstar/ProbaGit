#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Calculadora senzilla

print ("Introduzca un número")
Num=float(input())
print ("Introduzca una operación(+ - * /)")
Op=raw_input()
print ("Introduzca otro número")
Num2=float(input())
Suma=Num+Num2
Resta=Num-Num2
Multi=Num*Num2

print ("Solución de su operación")
if Op=="+":
	print Suma
if Op=="-":
	print Resta
if Op=="*":
	print Multi
if Op=="/":
	while Num2==0:
		print ("No se puede calcular, Introduzca otro número")
		Num2=float(raw_input())
		Div=Num/Num2
	Div=Num/Num2
	print Div
	
