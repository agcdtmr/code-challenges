B=print
import sys as C
E=C.argv[1:]
if len(E)==0:B('Requires an integer as input');C.exit()
elif len(E)>1:B('Stop being greedy');C.exit()
try:A=int(E[0])
except ValueError:B('Unable to parse integer');C.exit()
if A==0:B('zero')
elif A>0:B(A*A)
elif A<0:
	F,D=0,1
	for G in range(-A):sum=F+D;F=D;D=sum
	B(D)