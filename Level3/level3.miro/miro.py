import sys
from collections import deque
n,m = list(map(int,input().split()))
cnt = []
for i in range(n):
    cnt.append(list(map(int,input())))
dx = [-1,1,0,0] #이동을 위한 방향 설정 x축
dy = [0,0,-1,1] #이동을 위한 방향 설정 y축
def bfs(a,b):
    queue = deque()
    queue.append((a,b)) #시작점으로 들어온 (a,b)를 queue에 넣는다.
    while(len(queue)!=0):   #queue안에 아무것도 없을때까지 반복문을 돈다.
        x,y = queue.popleft()   #queue 맨앞에 있는 인덱스를 꺼내서 시작점으로 지정한다.
        for i in range(4):  #4방향을 돌기위해 range를 4로 지정
            nx = x + dx[i]  #x 이동
            ny = y + dy[i]  #y 이동
            if nx<0 or ny<0 or nx>=n or ny>=m:  #배열의 범위를 넘어가면 continue
                continue
            if cnt[nx][ny]==0:  #0이 나와 벽에 막히면 continue
                continue
            if cnt[nx][ny]==1:  #길이라면
                cnt[nx][ny] = cnt[x][y]+1   #이전에 왔던 길에서 한칸 더온 것이기 때문에 이전 값에 1을 추가한 값으로 초기화
                queue.append((nx,ny))   #길을 queue에 넣음
bfs(0,0)
print(cnt)
