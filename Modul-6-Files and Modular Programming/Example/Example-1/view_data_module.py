def tampilkanmenu(listmenu):
  print('---------------Daftar Menu-------------------\n'+
  '\t Nama Menu \t Harga\n')
  # \t adalah jenis format print yang sama dengan satu kali tab
  for i in range(len(listmenu)):
    # selain format(), dapat digunakan %{format} yang dapat dialamatkan ke satu variabel
    print('\t %s \t Rp%s,00' %(listmenu[i][0],listmenu[i][1]))
  print('---------------------------------------------\n')
