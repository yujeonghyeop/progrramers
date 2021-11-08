def solution(n):
    answer = 0
    cnt=0
    for i in range(1,n+1):
        for j in range(i,n+1):
            cnt=cnt+j
            if cnt==n:
                answer+=1
                cnt=0
                break
            elif cnt>n:
                cnt=0
                break
    return answer
