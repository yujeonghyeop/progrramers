board= [[1, 2, 0, 0], [1, 0, 2, 0], [1, 0, 0, 0], [1, 0, 0, 1]]

[[1,2,0,0],[1,0,2,0],[1,0,0,0],[1,0,0,1]]
[[0, 0, 1, 0, 0, 0], [0, 2, 0, 0, 0, 1], [0, 0, 2, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0]]
k = 2
ax =0
ay = 2
bx = 0
by=3
from collections import deque

def bfs(a,b,visited,answer):
    q = deque()
    q.append([a,b])
    visited[a][b] = 0
    while(len(q)!=0):
        x,y = q.popleft()
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if ddx < 0 or ddy < 0 or ddx >= N or ddy >= N:
                continue
            elif danger[ddx][ddy] == 1 or danger[ddx][ddy] ==2 :
                continue
            elif danger[ddx][ddy] == 3 and visited[ddx][ddy] == -1:
                visited[ddx][ddy] = visited[x][y] + 1
                q.append([ddx,ddy])
            elif danger[ddx][ddy] == 0 and visited[ddx][ddy] == -1:
                visited[ddx][ddy] = visited[x][y] + 1
                answer.append([ddx,ddy,visited[ddx][ddy]])
                q.append([ddx,ddy])

N = len(board)
danger = [[0 for _ in range (N)] for _ in range(N)]
visited_a = [[-1 for _ in range (N)] for _ in range(N)]
visited_b = [[-1 for _ in range (N)] for _ in range(N)]
answer_a = []
answer_b = []
answer = 0
tmp_answer = []
dx = [-1,0,1,0]
dy = [0,-1,0,1]
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            for p in range(4):
                nx = i
                ny = j
                danger[nx][ny] = 1
                for q in range(k):
                    nx = nx + dx[p]
                    ny = ny + dy[p]
                    if nx <0 or ny < 0 or nx >=N or ny >= N:
                        break
                    elif board[nx][ny] == 2:
                        break
                    elif board[nx][ny] == 0:
                        danger[nx][ny] = 3 
        elif board[i][j] == 2:
            danger[i][j] = 2
print(danger)
bfs(ax,ay,visited_a,answer_a)
bfs(bx,by,visited_b,answer_b)
print(answer_a)
print(answer_b)
if answer_a[0][0] == answer_b[0][0] and answer_a[0][1] == answer_b[0][1]:
    if answer_a[1][2] >= answer_b[1][2]:
        tmp_answer.append(answer_a[0][2])
        tmp_answer.append(answer_b[1][2])
    elif answer_a[1][2] <= answer_b[1][2]:
        tmp_answer.append(answer_b[0][2])
        tmp_answer.append(answer_a[1][2])

else:
    tmp_answer.append(max(answer_b[0][2], answer_a[0][2]))
print(max(tmp_answer))