def divOrMod(bil1,bil2,operator):
  if operator=='division':
    return bil1/bil2
  elif operator=='modulo':
    return bil1%bil2
  else:
    return 'error: unknown operator'

def main():
  num1,num2,oprt=int(input('Bilangan 1: ')),int(input('Bilangan 2: ')),input('Operator: ')
  print('Hasil: ',divOrMod(num1,num2,oprt))

if __name__ == '__main__':
	main()
