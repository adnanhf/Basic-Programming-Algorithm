myinput=int(input('Masukkan n: '))
result=1
if myinput==0:
  print(str(myinput)+'! =',result)
else:
  for i in range(myinput,1,-1):
    result*=(i)
  print(str(myinput)+'! =',result)
