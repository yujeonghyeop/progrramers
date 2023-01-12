from collections import deque

def solution(storey):
    result = 0
    cnt = len(str(storey))
    strstorey = deque(list(str(storey)))
    for i in range(cnt-1,-1,-1):
        if i==0:
            if int(strstorey[i]) >= 6:
                result += 10 - int(strstorey[i])
                strstorey[i] = "0"
                strstorey.appendleft("1")
        if (int(strstorey[i])==5 and int(strstorey[i-1])>=5):
            result += 10 - int(strstorey[i])
            strstorey[i] = "0"
            strstorey[i-1] = str(int(strstorey[i-1])+1)
        if int(strstorey[i]) >= 6:
            result += 10 - int(strstorey[i])
            strstorey[i] = "0"
            strstorey[i-1] = str(int(strstorey[i-1])+1)
    realfllor = int(''.join(strstorey))
    while(realfllor!=0):
        realcnt = len(str(realfllor))
        minusfloor = (10**(realcnt-1))
        realfllor -= minusfloor
        result+=1
    return result