# data adalah list dari list subjek, predikat, dan objek
def cekdiksi(data,filename):
  print('----------------------------------------------------------------------------\n')
  print('                                Cek Kata\n')
  print('----------------------------------------------------------------------------\n')
  tocheck=input('Input kata: ')

  # pengecekan lokasi list dari kata yang dicek
  if tocheck in data[0]:
    label='subjek'
    print(tocheck,'merupakan salah satu kata yang dikenali komputer'+
      'diksi tersebut diberi label',label,'oleh komputer')
  elif tocheck in data[1]:
    label='predikat'
    print(tocheck,'merupakan salah satu kata yang dikenali komputer'+
      'diksi tersebut diberi label',label,'oleh komputer')
  elif tocheck in data[2]:
    label='objek'
    print(tocheck,'merupakan salah satu kata yang dikenali komputer'+
      'diksi tersebut diberi label',label,'oleh komputer')
  else:
    # jika kata tidak dikenali, maka cetak print di bawah ini
    print('maaf, komputer belum mengenali, silakan cek kata lainnya')

    # dan tanyakan apakah user ingin menambahkan kata tersebut ke dalam kamus
    cek=input('atau munkin ingin menambahkan isi kamus? ')
    # jika user menjawab ya dengan simbol di dalam list di bawah,
    # maka panggil prosedur tambahdiksi()
    if cek in ['ya','y','Y','yes']:
      tambahdiksi(data[0],data[1],data[2],filename)
  print('----------------------------------------------------------------------------\n\n')

def tambahdiksi(subject,predicate,objek,file):
  n=int(input('Jumlah inputan merupakan berapa kalimat yang akan diinput oleh user\n'+
    'Jumlah inputan yang diinginkan: '))

  # tambahkan unsur kalimat ke dalam masing-masing list
  for i in range(n):
    subject.append(input('Input subject: '))
    predicate.append(input('Input predicate: '))
    objek.append(input('Input object: '))

  # tulis ulang data di dalam file
  f=open(file,'w')
  for i in range(len(subject)):
    if i==len(subject)-1:
      # format penulisan data jika baris data saat ini merupakan baris terakhir
      f.write('%s/%s/%s' %(subject[i],predicate[i],objek[i]))
    else:
      # format penulisan data jika baris data saat ini bukan baris terakhir
      f.write('%s/%s/%s:' %(subject[i],predicate[i],objek[i]))
  f.close()

# data mentah adalah data yang belum dipisahkan antar atribut
def hapusdiksi(listofrawdata,filename):
  target=input('Masukkan keyword untuk menghapus satu kalimat\n'+
    'keyword: ')

  # buat list baru yang berisi data mentah yang tidak dihapus
  for i in range(len(listofrawdata)):
    new=[listofrawdata[i] for i in range(len(listofrawdata)) if target not in listofrawdata[i]]

  # tulis ulang file txt
  f=open(filename,'w')
  for i in range(len(new)):
    if i==len(new)-1:
      f.write('%s' %(new[i]))
    else:
      f.write('%s:' %(new[i]))
