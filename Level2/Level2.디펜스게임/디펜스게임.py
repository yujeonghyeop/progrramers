import heapq
def solution(n, k, enemy):
    maxhepq = []
    round = 0
    for i in range(len(enemy)):
        if n < enemy[i] and k <= 0:
            break
        if n>= enemy[i]:
            n -= enemy[i]
            heapq.heappush(maxhepq, -enemy[i])
        elif n < enemy[i] and k > 0:
            if len(maxhepq)==0:
                k -=1
            else:
                cnt = -heapq.heappop(maxhepq)
                if cnt > enemy[i]:
                    k-=1
                    n += cnt-enemy[i]
                    heapq.heappush(maxhepq,-enemy[i])
                else:
                    k-=1
                    heapq.heappush(maxhepq,-cnt)
        round += 1
    return round