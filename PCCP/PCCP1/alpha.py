def solution(input_string):
    check = {}
    notanswer = []
    answer = []
    checkstring = list(set(input_string))
    result = ""
    for i in input_string:
        if i not in check:
            check[i] = 1
        else:
            check[i] += 1
    for j in range(len(input_string)):
        cnt = 1
        point = j
        while(point<len(input_string)-1):
            if input_string[point] == input_string[point+1]:
                cnt += 1
                point +=1
            else:
                break
        if cnt == check[input_string[j]] or check[input_string[j]]<2:
            notanswer.append(input_string[j])
    for k in checkstring:
        if k not in notanswer:
            answer.append(k)
    if len(answer) == 0:
        result += "N"
    else:
        result += ''.join(sorted(list(set(answer))))
    return result
