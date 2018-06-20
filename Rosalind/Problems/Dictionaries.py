#!/usr/bin/python3
import re

dico={}
filename=input("Entre le document \n")
file=open(filename,"r")

for line in file:
	liste=line.split()
	for i in liste:
		if i in dico:
			a=int(dico[i])+1
			dico[i]=a
		else:
			dico[i]='1'

out=open("textO.txt", "w")
for key, value in dico.items():
	out.write('%s %s\n'%(key,value))
out.close()
