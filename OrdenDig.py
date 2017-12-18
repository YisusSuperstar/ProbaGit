#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Medico virtual

print ("Hola, soy tu médico virtual")
print ("Digame su edad")
Edad=int(input())
print ("Presenta estornudos?")
Est=raw_input()
print ("Tiene dolor de cabeza")
Dc=raw_input()
print ("Tiene problemas de estomago?")
Pe=raw_input()
print ("Tiene tos?")
Tos=raw_input()
if Est=="Si" or "si" and Dc=="Si" or "si" and Pe=="Si" or "si":
	print ("Tómate un paracetamol")
if Est=="Si" or "si" and Dc=="Si" or "si" and Pe=="no" or "No":
	print ("Tómate un ácido acetílico salicílico")
if Edad>"12" and Tos=="Si" or "si":
	print ("Cómete un caramelo de miel")
if Edad<"12" and Tos=="Si" or "si":
	print ("Cómete un caramelo de eucalipto")	
else:
	("Ven a mi consluta")
