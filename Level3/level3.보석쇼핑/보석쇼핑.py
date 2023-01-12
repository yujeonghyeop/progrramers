def solution(gems):
    length = len(set(gems)) #8 but index 7
    left, right = 0, 0
    gemdict = {gems[0] : 1}
    mingem = 99999
    answer = []
    while(left < len(gems) and right < len(gems)):
        if len(gemdict) == length:
            if right - left <= mingem:
                mingem = right-left
                answer.append([left+1,right+1])
            gemdict[gems[left]] -= 1
            if gemdict[gems[left]] == 0:
                del gemdict[gems[left]]
            left+=1
        else:
            right+=1
            if right == len(gems):
                break
            if gems[right] in gemdict:
                gemdict[gems[right]] +=1
            else:
                gemdict[gems[right]] = 1
    answer = sorted(answer,key=lambda x:(x[1]-x[0],x[0]))
    if len(answer) == 0:
        answer.append([1,len(gems)])
    return answer[0]