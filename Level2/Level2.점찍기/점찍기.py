import math
def solution(k, d):
    limit = (d//k) * k  # 4
    count =0 
    for i in range(0,limit+1,k):
        street = math.trunc((d**2 - i**2)**(1/2))
        count = count + (street//k) + 1
    return count