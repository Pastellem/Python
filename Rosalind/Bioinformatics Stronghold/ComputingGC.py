#!/usr/bin/python
#!/usr/bin/python3
# -*- coding: latin-1 -*-

import re
import os

filename=input("Give DNA string in FASTA format :\n")
file=open(filename,"r")
gc=0
GC=0
Gc=0
name=''
liste=''
i=0

for line in file:
	if re.match('>', line):
		part=re.findall('[a-zA-Z]*_[\d]*',line)
		name=part.pop()
	else:
		sequence=''
		while re.match('^[^>]',line):
			part=re.split('\s',line)
			sequence+=part[0]
			line=file.readline()
		gc=re.findall('[GC]',sequence)
		Gc=len(gc)/len(sequence)*100
		if Gc > i and Gc>GC:
			liste=name
			GC=Gc
		if Gc==i and Gc == GC:
			liste+=name
		part=re.findall('[a-zA-Z]*_[\d]*',line)
		if not part:
			break
		else:
			name=part.pop()
	i=Gc
print('%s\n%s'%(liste,round(GC,6)))
file.close()



