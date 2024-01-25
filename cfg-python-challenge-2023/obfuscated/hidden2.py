A=print
import sys as B
D=B.argv[1:]
if len(D)==0:A('Requires an integer as input');B.exit()
elif len(D)>1:A('Stop being greedy!');B.exit()
try:C=int(D[0])
except ValueError:A('Unable to parse number');B.exit()
if C==0:A('zero')
elif C%2:A(C-1)
else:A(C+2)