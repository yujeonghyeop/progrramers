import itertools
import math

def prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    numbers=list(numbers)
    answer=[]
    cnt=[]
    for i in range(1,len(numbers)+1):
        cnt.append(list(map(''.join, itertools.permutations(numbers,i))))
    for i in range(len(cnt)):
        cnt[i]=list(set(cnt[i]))
        for j in range(len(cnt[i])):
            if int(cnt[i][j])==1 or int(cnt[i][j])==0:
                continue
            else:
                if prime(int(cnt[i][j])):
                    answer.append(int(cnt[i][j]))
    return len(set(answer))