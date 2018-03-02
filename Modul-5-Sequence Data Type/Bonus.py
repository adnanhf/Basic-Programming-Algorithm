def makeMatrix(ordo):
  return [[int(input('element[%s]: ' %idx2)) for idx2 in range(ordo)] for idx1 in range(ordo)]

def matrixInverse(mat):
  det = (mat[0][0]*mat[1][1])-(mat[0][1]*mat[1][0])
  adj = [[mat[1][1], -mat[0][1]], [-mat[1][0], mat[0][0]]]
  return [[(1/det)*adj[i][j] for j in range(len(mat))] for i in range(len(mat))]

def multiplyMatrix(mat1,mat2):
  res=[[0,0],[0,0]]
  # iterate through rows of mat1
  for i in range(len(mat1)):
    # iterate through columns of mat2
    for j in range(len(mat2[0])):
      # iterate through rows of mat2
      for k in range(len(mat2)):
        res[i][j] += mat1[i][k] * mat2[k][j]

  return res

def main():
  myordo=int(input('Input ordo: '))
  print('Matrix A')
  mymatrix1=makeMatrix(myordo)
  print('Matrix B')
  mymatrix2=makeMatrix(myordo)
  myinv=matrixInverse(mymatrix2)
  print('Inverse of Matrix B:',myinv)
  result=multiplyMatrix(mymatrix1, myinv)
  print('Division Result:', result)

if __name__ == '__main__':
  main()
