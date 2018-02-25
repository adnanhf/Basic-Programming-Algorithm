def faktorial(n):
  hasil=1
  for idx in range(n):
    hasil*=(idx+1)
  return hasil

def kombinasi(n,r):
  return faktorial(n)/(faktorial(r)*faktorial(n-r))

def main():
  a,b=int(input("masukkan n: ")),int(input("masukkan r: "))
  output=kombinasi(a,b)
  print(output)

if __name__ == '__main__':
  main()
