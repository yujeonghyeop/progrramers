v = [[1,4],[3,4],[3,10]]
dict_x = {}
dict_y = {}
answer = []
for i in range(len(v)):
    if v[i][0] not in dict_x:
        dict_x[v[i][0]] = 1
    else:
        dict_x[v[i][0]] +=1
for j in range(len(v)):    
    if v[j][1] not in dict_y:
        dict_y[v[j][1]] = 1
    else:
        dict_y[v[j][1]] +=1
for k,v in dict_x.items():
    if v ==1:
        answer.append(k)
for k,v in dict_y.items():
    if v ==1:
        answer.append(k)
print(answer)
