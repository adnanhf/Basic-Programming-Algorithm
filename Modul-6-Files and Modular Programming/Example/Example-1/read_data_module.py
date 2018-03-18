def readfile(filetoread):
  f=open(filetoread,'r')
  # membaca seluruh isi data
  content=f.read()
  # simbol ':' adalah penanda baris, syntax di bawah ini akan memisahkan string berdasarkan ':'
  filteredcontent=content.split(':')
  # setiap baris memiliki dua atribut, yaitu nama menu dan harga, keduanya dipisahkan oleh koma
  morefilteredcontent=[filteredcontent[x].split(',') for x in range(len(filteredcontent))]
  f.close()
  
  # mengembalikan nested list daftar menu
  return morefilteredcontent
