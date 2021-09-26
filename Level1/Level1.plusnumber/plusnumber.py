def solution(absolutes, signs):
    answer = 0
    signs=list(signs)
    for i in range(0,len(absolutes)):
        if signs[i]==True :
            answer+=absolutes[i]
        else:
            answer-=absolutes[i]
    return answer