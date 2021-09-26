def solution(d, budget):
    answer = 0
    d=sorted(d)
    for i in range(1,len(d)+1):
        if sum(d[:i])<=budget:
            answer+=1
    return answer