#!/usr/bin/python
#!/usr/bin/python3
# -*- coding: latin-1 -*-

import sys

n=int(input("Nomber of month :"))
k=int(input("Numers of offspring :"))
total=0


def Fibonnacci(i,k): #initiallisation n month, k offspring
	if i==0:
		return 0
	if i==1:
		return 1
	else:
		return Fibonnacci(i-1,k)+Fibonnacci(i-2,k)*k
	
for month in range(0,n):
	Fibonnacci(month,k)
	if month!=0:
		total=(Fibonnacci(month,k)+Fibonnacci(month-1,k)*k)
print(total)
		

