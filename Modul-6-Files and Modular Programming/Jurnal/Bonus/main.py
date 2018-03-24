# f1 = open('MatrixA.txt','r')
# f2 = open('MatrixB.txt','r')

# m1,m2=json.load(f1),json.load(f2)
# result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*m2)] for X_row in m1]
# print(m1,'\n',m2,'\n',numpy.shape(m1),numpy.shape(m2),'\n',result)
import module as m

m1 = m.read('MatrixA')
m2 = m.read('MatrixB')

result = m.multiple(m1, m2)

m.write(result, 'MatrixC')