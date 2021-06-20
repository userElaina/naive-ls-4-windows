import os
import sys
import random

exts={
	'':[''],
	'qwq':['qwq','qwq1','qwq2','qwq3','qwq4','bmp'],
	'pic':['png','jpg','jpeg','gif','bmp','tif','tiff'],
	'tar':['rar','zip','7z','tar','gz','xz','z','bz2'],
	'music':['mp3','wav','flac'],
	'movie':['mp4','mkv','mov','ts'],
	'office':['csv','doc','docx','ppt','pptx','xls','xlsx','pdf'],
	'danger':['vbs','sh','cmd','exe'],
	'html':['html'],
	'txt':['txt','in','out','log'],
	'data':['xml','json','svg','csv','md','rst'],
	'c':['c','cpp','h','hpp'],
	'java':['java'],
	'py':['pyi','py'],
	'othercodes':['cs','go','js','lua','pas','php','r','rb','swift','ts','vb','sh','vbs'],
}
exts['muz']=exts['music']
exts['vid']=exts['movie']
exts['cpp']=exts['c']
exts['python']=exts['py']
exts['codes']=exts['c']+exts['java']+exts['py']+exts['othercodes']+exts['data']
exts['text']=exts['codes']+exts['txt']+exts['html']

colors={
	'default':'\033[0m',
	'red':'\033[31m',
	'green':'\033[32m',
	'yellow':'\033[33m',
	'blue':'\033[34m',
	'purple':'\033[35m',
	'cyan':'\033[36m',
}

color_name={
	'dft':'default',
	'rd':'red',
	'yl':'yellow',
	'pp':'purple',
	'ppl':'purple'
}

for i in colors:
	color_name[i]=i
	color_name[i[0]]=i
	color_name[i[:2]]=i


class Ls:
	def __init__(
		self,
		pth:str='./',
		l:list=list(),
	):
		self.__pth=os.path.abspath(pth)

		self.__d=['.','..',]
		self.__f=list()
		self.__ext=list()
		for i in os.listdir(self.__pth):
			i=os.path.join(self.__pth,i)
			if os.path.isdir(i):
				self.__d.append(i)
			elif os.path.isfile(i):
				self.__f.append(i)
				self.__ext.append(
					i.rsplit('.',1)[-1].lower() if '.' in os.path.basename(i) else ''
				)
		self.__len=(len(self.__d)-2,len(self.__f))
		self.__ans=0
		self.__col=['default']*self.__len[1]

		self.__cols={'red','green','yellow','blue','purple','cyan'}

		for i in l:
			if isinstance(i,str):
				self.paint(i)
			else:
				self.paint(i[0],i[1])

	def __get_col(self)->str:
		ans=random.choice(list(self.__cols))
		if len(self.__cols)>1:
			self.__cols.discard(ans)
		return ans

	def paint(self,x:str,y:str=None):
		if y in color_name:
			y=color_name[y]
		else:
			y=self.__get_col()
		l_ext=exts[x]
		for i in range(self.__len[1]):
			if self.__ext[i] in l_ext:
				self.__col[i]=y
		self.__ans=len([None for i in self.__col if i!='default'])
		
	
	def to_dict(self)->dict:
		return {'dir':self.__d,'file':self.__f,}

	def show(self):
		print('\ndir('+str(self.__len[0])+'):\n')
		for i in self.__d:
			print(os.path.basename(i)+'/')
		print('\033[0m')
		print('file('+str(self.__ans)+'/'+str(self.__len[1])+'):\n')
		for i in range(self.__len[1]):
			print(colors[self.__col[i]]+os.path.basename(self.__f[i])+'\n'+colors['default'],end='')
		print()

	def fullshow(self):
		print('\ndir('+str(self.__len[0])+'):\n')
		for i in self.__d:
			print(i+'/')
		print('\033[0m')
		print('file('+str(self.__ans)+'/'+str(self.__len[1])+'):\n')
		for i in range(self.__len[1]):
			print(colors[self.__col[i]]+self.__f[i]+'\n'+colors['default'],end='')
		print()

cd='./'
l=sys.argv[1:]
if len(l):
	if os.path.isdir(l[0]):
		cd=l.pop(0)
mian=Ls(cd)

for i in l:
	x=i
	y=None
	for j in '=.-_:':
		if j in i:
			x=i.split(j)[0]
			y=i.split(j)[-1]
	mian.paint(x,y)
mian.show()
