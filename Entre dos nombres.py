#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Entre dos nombres

print "Introduzca un número"
Num=int(input())
print "Introduzca otro número"
Num2=int(input())
print ("Los números entre estos dos dígitos són:")
if Num<Num2:
	for i in range(Num+1,Num2,1):
		print i
if Num>Num2:
	for i in range(Num2+1,Num,1):
		print i	
