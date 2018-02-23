bil1 = int(input("Bilangan 1 : "))
bil2 = int(input("Bilangan 2 : "))
bil3 = int(input("Bilangan 3 : "))

if bil1<bil2<bil3 :
	print("Terbesar :", bil3)
	print("Terkecil :", bil1)
elif bil1<bil3<bil2 :
	print("Terbesar :", bil2)
	print("Terkecil :", bil1)
elif bil2<bil1<bil3 :
	print("Terbesar :", bil2)
	print("Terkecil :", bil2)	
elif bil2<bil3<bil1 :	
	print("Terbesar :", bil1)
	print("Terkecil :", bil2)
elif bil3<bil1<bil2 :
	print("Terbesar :", bil2)
	print("Terkecil :", bil3)
elif bil3<bil2<bil1 :
	print("Terbesar :", bil1)
	print("Terkecil :", bil3)

'''
# Mencari yang terbesar
if bil1>bil2 and bil1> bil3 :
    print("Terbesar :", bil1)
elif bil2>bil1 and bil2>bil3 :
    print("Terbesar :", bil2)
else:
    print("Terbesar :", bil3)

# Mencari yang terkecil
if bil1<bil2 and bil1 < bil3 :
    print("Terkecil :", bil1)
elif bil2 < bil1 and bil2 < bil3 :
    print("Terkecil :", bil2)
else:
    print("Terkecil :", bil3)
'''    
