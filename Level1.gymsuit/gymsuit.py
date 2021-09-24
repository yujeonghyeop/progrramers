def solution(n, lost, reserve):
    answer = n-len(lost)
    lost=sorted(lost)
    reserve=sorted(reserve)
    for i in lost[:]:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
            answer+=1
    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            answer+=1
        elif lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            answer+=1
    return answer