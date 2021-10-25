from math import gcd
def solution(arr):
    answer=1
    arr=sorted(arr)
    for i in range(len(arr)-1):
        arr[-2]=(arr[-1]*arr[-2])//gcd(arr[-1],arr[-2])
        arr.pop()
        if len(arr)==2:
            answer=answer*(arr[-1]*arr[-2])//gcd(arr[-1],arr[-2])
    return answer