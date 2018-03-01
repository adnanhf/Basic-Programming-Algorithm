mydict,n={},int(input('n: '))
for idx in range(n):
  mykey=input('key %s: ' %(idx+1))
  mydict[mykey]=input('value %s: ' %(idx+1))

print(mydict)
