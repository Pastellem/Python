#!/usr/bin/python3
k=m=n=2
#k=21 
#m=19
#n=16
import re
import os

filename=input("Data population :\n")
file=open(filename,"r")

for line in file:
	valeur=re.split('\s',line)
	k=int(valeur[0])
	m=int(valeur[1])
	n=int(valeur[2])
file.close()

pop=k+m+n

Pk=k/pop
Pm=m/pop
Pn=n/pop

Pk1=(k-1)/(pop-1)
Pm1=(m-1)/(pop-1)
Pn1=(n-1)/(pop-1)

Pk2=(k)/(pop-1)
Pm2=(m)/(pop-1)
Pn2=(n)/(pop-1)

k=1/4
n=2/4
m=3/4

PK=(Pk*Pk1)+(Pk*Pm2)+(Pk*Pn2)
PM=(Pm*Pm1*m)+(Pm*Pk2)+(Pm*Pn2*n)
PN=(Pn*Pm2*n)+(Pk2*Pn)

print(round((PK+PM+PN),6))
