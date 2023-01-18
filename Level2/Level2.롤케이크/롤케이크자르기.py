from collections import deque

def solution(topping):
    topping = deque(topping)
    older = {}
    for i in topping:
        if i not in older:
            older[i] = 1
        else:
            older[i] +=1
    count = len(older)
    answer = 0
    younger = {}
    for i in range(len(topping)):
        a = topping.popleft()
        if a not in younger:
            younger[a] = 1
        else:
            younger[a] += 1
        if a in older:
            older[a] -= 1
        if older[a] == 0:
            del older[a]
        if len(older) == len(younger):
            answer +=1
    return answer
