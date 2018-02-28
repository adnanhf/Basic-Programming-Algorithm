def filterGanjil(a_list):
  return [a_list[idx] for idx in range(len(a_list)) if a_list[idx] % 2 != 0]

def main():
  a, b = int(input('Masukkan A:')), int(input('Masukkan B:'))
  L = [idx for idx in range(a, b + 1)]
  L2 = filterGanjil(L)
  print('', L, '\n', L2)

if __name__ == '__main__':
  main()
