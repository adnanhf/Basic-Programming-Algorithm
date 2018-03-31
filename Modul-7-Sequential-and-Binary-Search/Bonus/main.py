from module import *

if __name__ == '__main__':
	file = openfile()
	viewfile(file)
	c = int(input('Input the value you want to search : '))
	binarySearch(file, c)
