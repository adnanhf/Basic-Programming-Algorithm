from read_data_module import *
import reserving_module
from view_data_module import *

def main():
  daftar_menu=readfile('temporar.txt')

  print('============================================================================\n'+
  '                             Warung Agak Mahal\n'+
  '============================================================================\n\n'+
  'Pilihan Aksi:\n'+
  '=======================\n'+
  '1. Terima Pesanan\n'+'2. Tampilkan Menu\n'+
  '=======================\n')

  pilihan_user=int(input('Input Aksi: '))

  if pilihan_user==1:
    bill=reserving_module.terimapesanan(daftar_menu)
    reserving_module.bayarpesanan(bill)
    main()
  elif pilihan_user==2:
    tampilkanmenu(daftar_menu)
  else:
    print('----Input Aksi Tidak Terdaftar, silakan Input Aksi kembali----\n\n')
    main()

if __name__ == '__main__':
  main()
