#!/usr/bin/python3

import io
import re

filename=input("Donnez le chemin du ficher")

file=open(filename, "r")
out=open("textrosalind.txt","w")
i=0
for line in file:
	if i%2!=0:
		out.write(line)
	i+=1
out.close()
