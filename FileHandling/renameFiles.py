import sys
from os import listdir, rename
from os.path import join , isfile
#print(os.listdir(sys.argv[1]))
for x in listdir(sys.argv[1]):
	fullPath = join(sys.argv[1],x)
	renamedFilePath = join(sys.argv[1],"file_{}".format(x)) 
	if isfile(fullPath): 
		print 'f-', x
		rename(fullPath,renamedFilePath)

