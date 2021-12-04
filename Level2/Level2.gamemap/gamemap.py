from collections import deque
def solution(maps):
    d = [[1,0],[-1,0],[0,1],[0,-1]]
    table = [[-1 for _ in range(len(maps[0]))]for _ in range(len(maps))]
    q=deque()
    q.append([0,0])
    table[0][0]=1
    while(q):
        y,x=q.popleft()
        for i in range(4):
            dy = y+d[i][0]
            dx = x+d[i][1]

            if -1<dy<len(maps) and -1<dx<len(maps[0]):
                if maps[dy][dx]==1:
                    if table[dy][dx]==-1:
                        table[dy][dx]=table[y][x]+1
                        q.append([dy,dx])
    return table[-1][-1]