#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Máquina expendedora de monedas
print ("Introduzca alguna cantidad de dinero")
Din=int(input())
Quin=0
Dosc=0
Cien=0
Cinc=0
Veint=0
Die=0
Cinco=0
Dos=0
Un=0
while Din>=500:
	Din=Din-500
	Quin=Quin+1
while Din>=200:
	Din=Din-200
	Dosc=Dosc+1
while Din>=100:
	Din=Din-100
	Cien=Cien+1
while Din>=50:
	Din=Din-50
	Cinc=Cinc+1
while Din>=20:
	Din=Din-20
	Veint=Veint+1
while Din>=10:
	Din=Din-10
	Die=Die+1
while Din>=5:
	Din=Din-5
	Cinco=Cinco+1
while Din>=2:
	Din=Din-2
	Dos=Dos+1
while Din>=1:
	Din=Din-1
	Un=Un+1
print Quin,"Billete/s de quinientos euros"
print Dosc,"Billete/s de doscientos euros"
print Cien,"Billete/s de cien euros"
print Cinc,"Billete/s de cincuenta euros"
print Veint,"Billete/s de veinte euros"
print Die,"Billete/s de diez euros"
print Cinco,"Billete/s de cinco euros"
print Dos,"Moneda/s de dos euros"
print Un,"Moneda/s de un euro"
	
	
		





































