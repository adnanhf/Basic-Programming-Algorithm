def readfile(filetoread):
  f=open(filetoread,'r')

  # membaca seluruh isi file
  content=f.read()

  # pemisahan baris data yang ditandai dengan simbol ':'
  filteredcontent=content.split(':')

  # pemisahan atribut data di setiap baris yang ditandai dengan simbol '/'
  morefilteredcontent=[filteredcontent[x].split('/') for x in range(len(filteredcontent))]

  # assignment unsur kalimat ke dalam 3 list terpisah
  subj=[morefilteredcontent[x][0] for x in range(len(morefilteredcontent))]
  pred=[morefilteredcontent[x][1] for x in range(len(morefilteredcontent))]
  obj=[morefilteredcontent[x][2] for x in range(len(morefilteredcontent))]
  f.close()
  return subj,pred,obj,filteredcontent

# data adalah list dari list subjek, predikat, dan objek
def viewfile(data):
  for i in range(len(data[0])):
    print('subjek:%s\tpredikat:%s\tobjek:%s' %(data[0][i],data[1][i],data[2][i]))