def Ds(mat):
    n=len(mat)
    s=0
    for i in range(n):
        s+=mat[i][i]
        s+=mat[i][n-i-1]

    if n%2==1:
        s=s-[n/2][n/2]

    return s

p=(int)input()
mat[p][p]
for i in range p:
    for j in range i:
        mat[i][j]=(int)input()

Ds(mat)
