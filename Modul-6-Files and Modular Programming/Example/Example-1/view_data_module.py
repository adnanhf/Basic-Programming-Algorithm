def tampilkanmenu(listmenu):
  print('---------------Daftar Menu-------------------\n'+
  '\t Nama Menu \t Harga\n')
  for i in range(len(listmenu)):
    print('\t %s \t Rp%s,00' %(listmenu[i][0],listmenu[i][1]))
  print('---------------------------------------------\n')
