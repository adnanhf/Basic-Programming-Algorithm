myinput=int(input('Masukkan n: '))
jml=0
for i in range(1, myinput*2, 2):
    print(i,end=' ')
    jml+=i
print('=',jml)
