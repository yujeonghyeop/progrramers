from math import gcd
def solution(arr):
    answer=1
    arr=sorted(arr) #우선 정렬먼저 해준다.
    for i in range(len(arr)-1): #2개씩 짝지어서 최소공배수를 구할 것이기 때문에 전체길이에서 1만큼 빼준횟수만 for문을 돌려준다.
        arr[-2]=(arr[-1]*arr[-2])//gcd(arr[-1],arr[-2]) #-2번쨰 인덱스를 -1과-2인덱스의 최소공배수로 설정하고
        arr.pop()   #-1인덱스를 날려버린다.
        if len(arr)==2: #만약 인덱스가 2개만 남았다면
            answer=answer*(arr[-1]*arr[-2])//gcd(arr[-1],arr[-2])   #answer에다 남은 2개의 최소공배수를 기록해준다.
    return answer