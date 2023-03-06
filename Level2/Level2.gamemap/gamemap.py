from collections import deque
def dfs(array,visited):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    q = deque()
    q.append([0,0])
    visited[0][0] = 1
    while(q):
        x,y = q.popleft()
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if ddx < 0 or ddx>=len(array) or ddy <0 or ddy >= len(array[0]):
                continue
            elif visited[ddx][ddy] != -1:
                continue
            elif array[ddx][ddy] == 0:
                continue
            else:
                q.append([ddx,ddy])
                visited[ddx][ddy] = visited[x][y] + 1

    return visited
def solution(maps):
    visited = [[-1]*len(maps[0]) for _ in range(len(maps))]
    answer = dfs(maps, visited)
    if answer[-1][-1] == 1:
        return -1
    else:
        return answer[-1][-1]