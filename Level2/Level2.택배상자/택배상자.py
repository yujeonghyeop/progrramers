from collections import deque

def solution(order):
    orders = deque(order)
    container = deque()
    sub = []
    for i in range(1,len(order)+1):
        container.append(i)
    result = 0
    orders.append(i+1)
    box = orders.popleft()
    while(True):
        if len(container)!=0:
            if container[0] <box:
                sub.append(container.popleft())
            elif container[0] == box:
                container.popleft()
                box = orders.popleft()
                result+=1
            elif container[0] > box:
                if sub[-1] == box:
                    sub.pop()
                    box = orders.popleft()
                    result+=1
                else:
                    break
        else:
            if len(sub) == 0:
                break
            else:
                if sub[-1] == box:
                    sub.pop()
                    box = orders.popleft()
                    result+=1
                else:
                    break
    return result