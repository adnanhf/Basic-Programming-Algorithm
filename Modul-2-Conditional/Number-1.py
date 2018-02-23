bil1 = int(input("Bilangan 1 : "))
bil2 = int(input("Bilangan 2 : "))
opt = input("Operator : ")

if opt == "+" :
    hasil = bil1+bil2
    print("hasil : ",hasil)
elif opt == "-":
    hasil = bil1-bil2
    print("hasil : ",hasil)
elif opt == "x":
    hasil = bil1*bil2
    print("hasil : ",hasil)
elif opt == ":" :
    hasil = bil1/bil2
    print("hasil : ",hasil)
else:
    print("operator tidak ditemukan atau inputan tidak sesuai format")
