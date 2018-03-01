def cekPalindrom(mystr):
  newstr=mystr[::-1]
  if mystr == newstr:
    return newstr,True
  else:
    return newstr,False

def main():
  mywords=input('Masukkan kata: ')
  newwords,palindrom=cekPalindrom(mywords)
  print('\ninput:',mywords,'\noutput:',newwords,'\nPalindrom:',palindrom,'\n')

if __name__ == '__main__':
  main()
