H=print
D=' '
import sys
E=sys.argv[1:]
if len(E)==0:H('I require a string as input');sys.exit()
input=D.join(E)
F=[]
B=True
for A in input.split(D):
	if len(A)<1:B=False;continue
	if B:A=A[::-1];B=True
	C=''
	for G in A:
		if G.isalnum():C+=G
		else:C+='-'
	F.append(C)
H(D.join(F))