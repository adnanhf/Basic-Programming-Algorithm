def readfile(filetoread):
  f=open(filetoread,'r')
  content=f.read()
  filteredcontent=content.split(':')
  morefilteredcontent=[filteredcontent[x].split(',') for x in range(len(filteredcontent))]

  return morefilteredcontent