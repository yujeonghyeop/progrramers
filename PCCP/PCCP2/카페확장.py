from collections import deque # 최대한 일반 사회에서의 구조와 비슷하게 만들어 주어야 한다.
def solution(menu, order, k): # 알바는 주문을 받고 만들 수 있는 상태이면 바로 만들어 주고
    dq = deque()# 만들수 없는 상태라면 손님이 대기하는 구조이기 때문에 이를 적용하여 만들어 준다
    waiting = deque()
    maketime = -1
    answer = 0
    for i in range(k*(len(order)-1)+1):
        if i == maketime:
            waiting.popleft()
            maketime = -1
        if i % k ==0:
            waiting.append(i//k)
        if maketime == -1 and len(waiting) != 0:
            maketime = i+menu[order[waiting[0]]]
        answer = max(answer, len(waiting))  
    return answer