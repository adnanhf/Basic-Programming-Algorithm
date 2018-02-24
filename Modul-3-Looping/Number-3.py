myinput = int(input("Input n : "))
for i in range(myinput+1):
  for j in range(i):
    print("*", end=" ")
  print()
for i in range(myinput):
  j=1
  while j < myinput-i:
    print("*",end=" ")
    j=j+1
  print()
