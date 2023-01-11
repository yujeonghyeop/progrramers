import heapq
def solution(ability, number):
    heapq.heapify(ability)
    for i in range(number):
        sum1 = ability[0] + ability[1]
        heapq.heappop(ability)
        heapq.heappop(ability)
        heapq.heappush(ability,sum1)
        heapq.heappush(ability,sum1)
    return sum(ability)