jarak = int(input("Jarak Tempuh : "))
harga = int(input("Harga Tiket : "))

if jarak > 300 or harga > 500000 :
    print("Harga Tiket :",harga*(50/100))
elif jarak > 200 or harga > 300000 :
    print("Harga Tiket : ",harga-(harga*(20/100)))
else:
    print("Harga Tiket : ",harga)
