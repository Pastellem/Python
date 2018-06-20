#!/usr/bin/python3
# -*- coding: latin-1 -*-

import re
import os

#filename=input("Give DNA string in FASTA format :\n")
file=open("test.fa","r")
gc=0
GC=0
sequence=''
name=''
liste=''
for line in file:
	if re.match('>', line):
		name=re.split('\s',line)
		print(name)
	if re.match('>',line)==None:
		while re.search('\d',line)==None or re.match('^\S',line):
			print('move')
			line=file.readline()
file.close()
#print('%s\n%s'%(liste,round(GC,6)))
#print(Gc)
