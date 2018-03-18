import read_and_view_data_module as rnv
from comparing_or_modify_module import *

def main():
  # format pemanggilan metode/fungsi/prosedur jika modul diimport dengan format syntax 'import [nama_module]'
  sub,pre,obj,raw=rnv.readfile('dict.txt')

  print('============================================================================\n'+
  '                           Kamus Linguistik Komputer\n'+
  '============================================================================\n\n'+
  'Pilihan Aksi:\n'+
  '=======================\n'+
  '1. Cek Kata\n2. Hapus Diksi\n3. Tampilkan Diksi\n'+
  '=======================\n')

  pilihan_user=input('Input Aksi: ')

  if pilihan_user=='1':
    # format pemanggilan metode/fungsi/prosedur jika modul diimport dengan format syntax 'from [nama_module] import *'
    cekdiksi([sub,pre,obj],'dict.txt')
    main()
  elif pilihan_user=='2':
    hapusdiksi(raw,'dict.txt')
    main()
  elif pilihan_user=='3':
    rnv.viewfile([sub,pre,obj])
    main()
  else:
    print('Aksi tidak valid, silakan ulangi lagi\n\n')
    main()

if __name__ == '__main__':
  main()