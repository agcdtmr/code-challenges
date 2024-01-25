F=print
E=' '
D=len
import sys
B=sys.argv[1:]
if D(B)==0:F('I require a string as input');sys.exit()
input=E.join(B)
input=B[0].lower()
C=[]
for A in input.split(E):
	if D(A)<1:continue
	elif D(A)==1:C.append(A.lower());continue
	G=A[0].upper();H=A[1:];C.append(G+H)
F(E.join(C))