def solution(s):
    answer = -1
    s=list(s)
    queue=['0']
    for i in range(len(s)):
        queue.append(s[i])
        if queue[-1]==queue[-2]:
            queue.pop()
            queue.pop()
    return 1 if len(queue)==1 else 0
