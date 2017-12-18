#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Analisis de nombre 
print "Introduzca su nombre"
Nom=raw_input()
for i in range(len(Nom)):
	CantCar=i+1
Voc=Nom.count("a")+Nom.count("e")+Nom.count("i")+Nom.count("o")+Nom.count("u")
print "Hay",CantCar,"Caracteres y",Voc,"Vocales en:",Nom

