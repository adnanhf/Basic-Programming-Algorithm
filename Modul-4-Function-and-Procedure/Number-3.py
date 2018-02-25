def toReamur(nilai_suhu):
  return (4/5)*nilai_suhu

def toFahren(nilai_suhu):
  return (9/5)*nilai_suhu+32

def toKelvin(nilai_suhu):
  return nilai_suhu+273

def konversiSuhu(input_user):
  print('in Reamur: ',toReamur(input_user),'R')
  print('in fahrenheit: ',toFahren(input_user),'F')
  print('in Kelvin: ',toKelvin(input_user),'K')

def main():
  x=int(input('Masukkan info suhu: '))
  konversiSuhu(x)

if __name__ == '__main__':
  main()
