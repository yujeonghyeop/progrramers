def solution(k, tangerine):
    cnt = 0
    answer = []
    orange = {}
    for i in tangerine:
        if i in orange:
            orange[i] += 1
        else:
            orange[i] = 1
    orange = sorted(orange.items(),key=lambda x:x[1], reverse=True)
    for i in range(len(orange)):
        if k <= 0:
            break
        if k > 0:
            k -= orange[i][1]
            answer.append(i)
    return len(answer)