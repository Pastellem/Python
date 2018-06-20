#!/usr/bin/python3

s='A1LWV51OW1OJ90uPsa6oy2NwOS2TICccaP0UeI77f609ds8VvY6KW14nFelEhnPbJPMustelanAmOx0DCUjpVFI8nkN0GpL1gOQdAdVO7VWZcmKvAfDfallax8GPDuOVPiuRSvQzEqgR8BYcMbp2ldSFge2KjnVG1Y3D0wJ'
a=66
b=72 
c=115 
d=120
s1=""
s2=""

for i in range(a,b+1):
	s1+=s[i]
for j in range(c,d+1):
	s2+=s[j]

print ('%s %s'%(s1, s2))
	
