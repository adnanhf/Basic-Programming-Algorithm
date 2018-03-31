def openfile():
	import json
	f = open('bonus.txt', 'r')
	val = json.load(f)
	return val

def viewfile(content):
	print(content)

def binarySearch(alist,item):
	alist.sort()
	first = 0
	last = len(alist)-1
	found = False
	print(alist)

	while first<=last and not found:
		middle = (first+last)//2
		if alist[middle] == item:
			found = True
		else:
			if item < alist[middle]:
				last=middle-1
			else:
				first=middle+1

	if found:
		print('Item found : ', item)
	else:
		print("Item not found!")
