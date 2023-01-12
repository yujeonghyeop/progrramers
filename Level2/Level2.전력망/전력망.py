n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
gr = {}
for i in wires:
    if i[0] in gr:
        gr[i[0]].append(i[1])
    else:
        gr[i[0]] = [i[1]]
    if i[1] in gr:
        gr[i[1]].append(i[0])
    else:
        gr[i[1]] = [i[0]]
print(gr)
#dict에서 가장 많은 숫자