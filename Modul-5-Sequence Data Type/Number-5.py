def matrixInvers(mat):
  det = (mat[0][0]*mat[1][1])-(mat[0][1]*mat[1][0])
  adj = [[mat[1][1], -mat[0][1]], [-mat[1][0], mat[0][0]]]
  return [[(1/det)*adj[i][j] for j in range(len(mat))] for i in range(len(mat))]

def main():
  matrix_ordo=int(input('masukkan ordo: '))
  mymatrix=[[int(input('element[%s]: ' %idx2)) for idx2 in range(matrix_ordo)] for idx1 in range(matrix_ordo)]
  myinv=matrixInvers(mymatrix)
  print(myinv)

if __name__ == '__main__':
  main()
