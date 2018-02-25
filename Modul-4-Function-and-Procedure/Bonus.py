def fromCelcius(valSuhu):
  return (4/5)*valSuhu,(9/5)*valSuhu+32,valSuhu+273
  
def fromReamur(valSuhu):
  return (5/4)*valSuhu,(9/4)*valSuhu+32,(5/4)*valSuhu+273

def fromFahren(valSuhu):
  return (5/9)*(valSuhu-32),(4/9)*(valSuhu-32),(5/9)*(valSuhu-32)+273
  
def fromKelvin(valSuhu):
  return valSuhu-273,(4/5)*(valSuhu-273),(9/5)*(valSuhu-273)+32

def konversiSuhu(input_user):
  nilai,skala=input_user.split()
  nilai=int(nilai)
  if skala == 'C':
    r,f,k=fromCelcius(nilai)
    print('in Reamur: ',r,' R')
    print('in Fahrenheit: ',f,' F')
    print('in Kelvin: ',k,' K')
  elif skala == 'R':
    c,f,k=fromReamur(nilai)
    print('in Celcius: ',c,' C')
    print('in Fahrenheit: ',f,' F')
    print('in Kelvin: ',k,' K')
  elif skala == 'F':
    c,r,k=fromFahren(nilai)
    print('in Celcius: ',c,' C')
    print('in Reamur: ',r,' R')
    print('in Kelvin: ',k,' K')
  elif skala == 'K':
    c,r,f=fromKelvin(nilai)
    print('in Celcius: ',c,' C')
    print('in Reamur: ',r,' R')
    print('in Fahrenheit: ',f,' F')

def main():
  x=input('Masukkan info suhu: ')
  konversiSuhu(x)

if __name__ == '__main__':
  main()
