n = 9
wires = [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]


def dfs(pica,visited,k,cnt,answer):
    if visited[k] == 0:
        visited[k] = 1
        for i in range(len(pica[k])):
            if pica[k][i] == 1:
                pica[k][i] == 0
                cnt +=1
                pica[i][k] == 0
                dfs(pica, visited, i,cnt,answer)
                pica[k][i] == 1
                pica[i][k] == 1
    answer.append(cnt)
pica = [[0]*(n+1) for _ in range(n+1)]
answer = []
realanswer = []
for i in wires:
    a,b = i
    pica[a][b] = 1
    pica[b][a] = 1
for i in wires:
    cnt = 0
    visited = [0] * (n+1)
    a,b = i
    pica[a][b] = 0
    pica[b][a] = 0
    dfs(pica,visited,a,cnt,answer)
    print(pica, "끊은 놈", a, "총 수", answer)
    pica[a][b] = 1
    pica[b][a] = 1
minanswer = 999999
best = n//2
answer = sorted(answer, key = lambda x: abs(best-x))
print(answer)

# for j in answer:
#     print(j, minanswer, best-j)
#     if abs(best-j)<minanswer:
#         minanswer = n-j
print(minanswer)