import os
import sys

from userelaina.cls import Ls

cd='./'
l=sys.argv[1:]
if len(l):
	if os.path.isdir(l[0]):
		cd=l.pop(0)

mian=Ls(cd)
full=False
no=False

for i in l:
	x=i
	y=None
	for j in '=.-_:':
		if j in i:
			x=i.split(j)[0]
			y=i.split(j)[-1]
	mian.paint(x,y)
	if i=='full':
		full=True
	if i=='no':
		no=True

mian.show(fullpath=full,no=no) 
