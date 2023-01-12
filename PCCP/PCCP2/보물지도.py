from numpy import ma


n = 4
m =4
hole =[[2,3],[3,3]]

mapp = [[0]*n for _ in range(m)]
print(mapp)
for i in hole:
    print(i)
    mapp[i[1]-1][i[0]-1] = 1
print(mapp)