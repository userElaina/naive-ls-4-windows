import os
import sys

_ext_d={
	'qwq':['qwq','qwq1','qwq2','qwq3','qwq4','bmp'],
	'pic':['png','jpg','jpeg','gif','bmp','tif','tiff'],
	'tar':['rar','zip','7z','tar','gz','xz','z','bz2'],
	'music':['mp3','wav','flac'],
	'movie':['mp4','mkv','mov','ts'],
}
_ext_d['muz']=_ext_d['music']
_ext_d['vid']=_ext_d['movie']

_ext=list()

if len(sys.argv)>1:
	if sys.argv[1] in _ext_d:
		_ext=_ext_d[sys.argv[1].replace(' ','').replace('-','')]

d=['.','..',]+[i for i in os.listdir() if os.path.isdir(i)]
f=[i for i in os.listdir() if os.path.isfile(i)]

a=[i for i in f if [None for j in _ext if i.lower().endswith('.'+j)]]

print('\ndir('+str(len(d)-2)+'):\n')
for i in d:print(i+'/')
print('\033[0m')
print('file('+str(len(a))+'/'+str(len(f))+'):\n')
for i in f:
	if [None for j in _ext if i.lower().endswith('.'+j)]:
		print('\033[33m'+i+'\n\033[0m',end='')
	else:
		print(i)

print()
