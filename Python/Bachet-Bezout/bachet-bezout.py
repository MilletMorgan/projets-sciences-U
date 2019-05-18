#!/usr/bin/python
# -*- coding: utf-8 -*-

#      bezout.py
#      
#      Last modif : 10.02.2008
#      
#      Copyright 2008 FranÃ§ois Magimel, alias Linkid <cucumania@gmail.com>
#      
#      This program is free software; you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation; either version 2 of the License, or
#      (at your option) any later version.
#      
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#      
#      You should have received a copy of the GNU General Public License
#      along with this program; if not, write to the Free Software
#      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#      MA 02110-1301, USA.

## Theoreme de BÃ©zout :
## Soient deux entiers relatifs a et b et d leur PGCD.
## Il existe deux entiers relatifs u et v tels que a.u + b.v = d.
## Et si a et b sont premiers entre eux, alors d=1 et donc a.u + b.v = 1

def affiche(liste):
	"fonction pour afficher les listes en colonne"
	for i in range(0, len(liste)):
		if liste[i] == ' ':
			print liste[i].rjust(4),
		else:
			print repr(liste[i]).rjust(4),

def bezout():
	"fonction qui calcul les coefficients de BÃ©zout et les affiche dans le tableau d'Euclide"
	a = input("Entrez le diviseur : ")
	b = input("Entrez le dividende : ")
	u0, u1 = 1, 0  ## a*1 + b*0 = a
	v0, v1 = 0, 1  ## a*0 + b*1 = b
	r = 1  ## reste fixÃ© Ã  1 au dÃ©part
	pgcd = 0  ## pgcd fixÃ© Ã  0 au dÃ©part
	zero = 0  ## pour vÃ©rifier si le calul du pgcd est possible ou non
	
	if ((a == 0) or (b==0)):
		if (a == b):
			pgcd, r = 0, 0 ## PGCD(0;0) = 0
		else:
			r, zero = 0, 1
			print "ON NE PEUT PAS DIVISER PAR 0" ## pour tout entier NON NUL n, PGCD(0;n)=impossible
	else:
		if (a % b == 0):
			pgcd = b  ## si a et b sont des diviseurs, alors le pgcd est le plus petit, ici b
	
	if (a < 0):
		a = -a  ## pgcd(-5;2) = pgcd(5;2)
	elif (b < 0):
		b = -b  ## pgcd(5;-2) = pgcd(5;2)
	
	quo = [' ']  ## liste des quotients
	divi = [a, b]  ## liste des diviseurs et dividendes
	rest = []  ## liste des restes
	coefu = [u0]  ## liste des coefficients u de bezout
	coefv = [v0]  ## liste des coefficients v de bezout
	
	while (r>0):
		q = a/b  ## quotient de la division
		r = a-(b*q)  ## reste de la division euclidienne
		u2 = (u0 - (q*u1))  ## coef u_{n+2}
		v2 = (v0 - (q*v1))  ## coef v_{n+2}
		## ajouts dans les listes
		quo.append(q)
		divi.append(r)
		rest.append(r)
		coefu.append(u1)
		coefv.append(v1)
		## on remplace les anciennes valeurs par les nouvelles
		a = b
		b = r
		u0, v0 = u1, v1
		u1, v1 = u2, v2
	
	if (zero == 0):
		print "\nquotient :           ",
		affiche(quo)
		print "\ndiviseur/dividende : ",
		affiche(divi)
		print "\nreste :              ",
		affiche(rest)
		print "\nu :                  ",
		affiche(coefu)
		print "\nv :                  ",
		affiche(coefv)
		if (pgcd != divi[1]):
			pgcd = rest[-2]  ## si pgcd est diffÃ©rent du premier dividende, alors pgcd = dernier reste non nul
		print "\n\nPGCD(" + str(divi[0]) + "; " + str(divi[1]) + ") = " + repr(pgcd)  ## conversion des int en str par deux mÃ©thodes pour afficher le PGCD


fin = 11  ## variable pour recommencer
bezout()  ## appel de la fonction bezout()
while (fin == 11):
	fin = input("\n\nTapez 11 pour recommencer et un autre chiffre pour quitter : ")
	if (fin == 11):
		bezout()  ## si fin est bien Ã©gal Ã  11, on recommence
