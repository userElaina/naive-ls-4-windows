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


def get_ext(s:str)->str:
	_base=os.path.basename(s)
	return _base.rsplit('.',1)[-1].lower() if '.' in _base else ''

class Ls:
	def __init__(
		self,
		pth:str='./',
		l:list=list(),
	):
		self.__pth=os.path.abspath('./')
		self.cd(pth)
		self.__col=dict()
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

	def cd(self,pth:str):
		_ans=os.path.abspath(os.path.join(self.__pth,pth))
		self.__pth=_ans if os.path.isdir(_ans) else os.path.dirname(_ans)
		self.__d=['.','..',]
		self.__f=list()
		self.__ext=list()
		for i in os.listdir(self.__pth):
			_full=os.path.join(self.__pth,i)
			if os.path.isdir(_full):
				self.__d.append(i)
			elif os.path.isfile(_full):
				self.__f.append(i)

	def paint(self,x:str,y:str=None)->bool:
		if x not in exts:
			return False
		y=color_name[y] if y in color_name else self.__get_col()
		_d={i:y for i in exts[x]}
		self.__col.update(_d)
		return True

	def get_pth(self)->str:
		return self.__pth

	def get_col(self)->list:
		return [self.__col.get(get_ext(i),'default') for i in self.__f]

	def get_ans(self)->list:
		return [i for i in self.__f if self.__col.get(get_ext(i),'default')!='default']

	def get_info(self)->dict:
		_col=self.get_col()
		_ans=self.get_ans()
		_d={
			'pth':self.__pth,
			'dir':self.__d,
			'file':self.__f,
			'ans':_ans,
			'dir_full':[os.path.join(self.__pth,i) for i in self.__d],
			'file_full':[os.path.join(self.__pth,i) for i in self.__f],
			'ans_full':[os.path.join(self.__pth,i) for i in _ans],
			'color':_col,
			'len_dir':len(self.__d)-2,
			'len_file':len(self.__f),
			'len_ans':len(_ans),
		}
		return _d

	def show(self,fullpath:bool=False):
		_d=self.get_info()
		_dir=_d['dir_full' if fullpath else 'dir']
		_file=_d['file_full' if fullpath else 'file']

		print()
		print(os.path.join(_d['pth'],''))
		print()
		print('dir('+str(_d['len_dir'])+'):')
		for i in _dir:
			print(os.path.join(i,''))
		print(colors['default'])

		print('file('+str(_d['len_ans'])+'/'+str(_d['len_file'])+'):')
		for i in range(_d['len_file']):
			print(colors[_d['color'][i]]+_file[i]+'\n'+colors['default'],end='')
		print()

cd='./'
l=sys.argv[1:]
if len(l):
	if os.path.isdir(l[0]):
		cd=l.pop(0)

mian=Ls(cd)
full=False

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

mian.show(fullpath=full)
