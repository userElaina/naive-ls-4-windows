import os
import sys

from userelaina.pthc import Ls

cd='./'
l=sys.argv[1:]
if len(l):
	if os.path.isdir(l[0]):
		cd=l.pop(0)

mian=Ls(cd)

full=False
num=False

for i in l:
	if i.startswith('-'):
		if 'full' in i:
			full=True
		if 'num' in i:
			num=True
		continue
	x=i
	y=None
	for j in ':=':
		if j in i:
			x=i.split(j)[0]
			y=i.split(j)[-1]
	mian.setcolor(x,y)

mian.show(fullpath=full,num=num)
