def terimapesanan(listmenu):
  # inisialisasi variabel
  pesen_lagi,list_pesanan,tagihan=True,[],0
  
  # selama masih pengen pesan, ya terus diulang
  while pesen_lagi:
    pesanan=input('Input Pesanan: ')
    # cek dulu menunya cocok ga sama menu di warung
    cek=[listmenu[x] for x in range(len(listmenu)) if pesanan in listmenu[x]]
    # kalo ada, akan ditambahkan ke dalam list pesanan
    list_pesanan.append(cek[0])
    lagi=input('Pesan Lagi? ')
    if lagi in ['Y','ya','yes']:
      pesen_lagi=True
    elif lagi in ['N','tidak','no']:
      pesen_lagi=False

  print('----------------------------------------------------------------------------\n'+
  'Daftar pesanan:\n'+
  '----------------------------------------------------------------------------')
  # menampilkan list pesanan pelanggan
  for i in range(len(list_pesanan)):
    print(i+1,list_pesanan[i][0])
    tagihan+=int(list_pesanan[i][1])
  print('----------------------------------------------------------------------------\n')

  print('Jumlah tagihan: Rp'+str(tagihan)+',00')

  return tagihan

def bayarpesanan(tagihan):
  bayar=int(input('Dibayar: Rp'))
  print('Uang Kembalian: Rp'+str(bayar-tagihan)+',00\n'+
  '------------------Terima Kasih, Sering-Sering Mampir ya---------------------\n\n')
