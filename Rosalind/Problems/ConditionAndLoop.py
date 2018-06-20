#!/usr/bin/python3

a=4076
b=8477
summary=0
for i in range(a,b+1):
	if i%2 !=0: #module give 0 if i was pair. If not i is odd integer
		summary+=i
print(summary)
