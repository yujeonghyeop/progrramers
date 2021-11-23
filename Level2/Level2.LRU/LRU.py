from collections import deque
def solution(cacheSize, cities):
    a=deque()
    time=0
    if cacheSize==0:
        return len(cities)*5
    else:
        for i in range(len(cities)):
            cities[i]=cities[i].lower()
            if cities[i] in a:
                if len(a)>=cacheSize:
                    a.remove(cities[i])
                a.append(cities[i])
                time+=1
            else:
                if len(a)>=cacheSize:
                    a.popleft()
                a.append(cities[i])
                time+=5
        return time