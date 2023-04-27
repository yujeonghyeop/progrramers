from collections import deque	

def dfs_L(a,b,maps,visited):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    q = deque()
    q.append([a,b])
    while(q):
        x,y = q.popleft()
        cnt = []
        for i in range(4):
            ddx = x+dx[i]
            ddy = y+dy[i]
            if ddx < 0 or ddx >=len(maps) or ddy < 0 or ddy >=len(maps[0]):
                continue
            elif maps[ddx][ddy] == 'X':
                continue
            elif maps[ddx][ddy] == 'O' or maps[ddx][ddy] == 'E':
                if visited[ddx][ddy] == 0:
                    visited[ddx][ddy] = visited[x][y] + 1
                    cnt.append([ddx,ddy])
            elif maps[ddx][ddy] == "L":
                visited[ddx][ddy] = visited[x][y] + 1
                return 
        for j in cnt:
            q.append(j)
def dfs_E(a,b,maps,toEndvisited):
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    q = deque()
    q.append([a,b])
    while(q):
        x,y = q.popleft()
        cnt = []
        for i in range(4):
            ddx = x+dx[i]
            ddy = y+dy[i]
            if ddx < 0 or ddx >=len(maps) or ddy < 0 or ddy >=len(maps[0]):
                continue
            elif maps[ddx][ddy] == 'X':
                continue
            elif maps[ddx][ddy] == 'O' or maps[ddx][ddy] == "E" or maps[ddx][ddy] == "S":
                if toEndvisited[ddx][ddy] == -1:
                    toEndvisited[ddx][ddy] = toEndvisited[x][y] + 1
                    cnt.append([ddx,ddy])
        for j in cnt:
            q.append(j)
def solution(maps):
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    toEndvisited = [[-1]*len(maps[0]) for _ in range(len(maps))]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                visited[i][j] == 1
                dfs_L(i,j,maps,visited)
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "L" and visited[i][j] != 0:
                toEndvisited[i][j] = visited[i][j]
                dfs_E(i,j,maps,toEndvisited)
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "E":
                return toEndvisited[i][j]