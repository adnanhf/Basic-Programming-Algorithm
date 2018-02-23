sms = input("Ketik SMS : ")
if sms[0:4] == "REG ":
  print("Selamat anda sudah terdaftar sebagai", sms[4:])
else:
  print("Maaf format anda salah")
