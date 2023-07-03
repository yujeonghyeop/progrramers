def solution(line):
    INF = float('inf')
    intersection = []
    answer = []
    minx = INF
    maxx = -INF
    miny = INF
    maxy = -INF
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            if ((line[i][0] * line[j][1]) - (line[i][1]*line[j][0])) !=0:
                x = ((line[i][1] * line[j][2]) - (line[i][2]*line[j][1])) / ((line[i][0] * line[j][1]) - (line[i][1]*line[j][0]))
                y = ((line[i][2] * line[j][0]) - (line[i][0] * line[j][2])) / ((line[i][0] * line[j][1]) - (line[i][1]*line[j][0]))
                if x%1 == 0.0 and y%1 == 0.0:
                    x = int(x)
                    y = int(y)
                    minx,maxx,miny,maxy = min(minx,x),max(maxx,x),min(miny,y),max(maxy,y)
                    intersection.append([x,y])

    star = [['.' for _ in range(0,maxx-minx+1)] for _ in range(0,maxy-miny+1)]
    for p in intersection:
        a,b = p
        star[maxy-b][a-minx] = '*'
    for q in range(0,len(star)):
        cnt = "".join(star[q])
        answer.append(cnt)
    return answer
