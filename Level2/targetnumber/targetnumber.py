def solution(numbers, target):
    answer = 0
    leaves=[0]
    for num in numbers:
        tmp=[]
        for parent in leaves:
            tmp.append(parent+num)
            tmp.append(parent-num)
        leaves=tmp
    for i in range(len(leaves)):
        if target==leaves[i]:
            answer+=1
    return answer
