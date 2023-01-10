ability = [
    [40, 10, 10], 
    [20, 5, 0], 
    [30, 30, 30], 
    [70, 0, 70], 
    [100, 100, 100]]
visited = [0]*len(ability)
answer = []
def dfs(ability, index,mymax, sum,ans):
    if index == len(ability[0]):
        if mymax <sum:
            mymax = sum
            answer.append(mymax)
        return 
    for i in range(len(ability)):
        if visited[i] == 1:
            continue
        visited[i] = 1
        sum += ability[i][index]
        dfs(ability,index+1,mymax, sum,ans)
        sum -= ability[i][index]
        visited[i] = 0
dfs(ability,0, 0,0,[])
print(sorted(answer)[-1])
