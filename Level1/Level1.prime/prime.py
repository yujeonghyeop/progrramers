import sys,math
def solution(n):
    prime=[True]*(n+1)
    prime[0]=False
    prime[1]=False
    m=int(math.sqrt(n+1))
    for i in range(2,m+2):
        if prime[i]==True:
            for j in range(i+i,n+1,i):
                prime[j]=False
    return prime.count(True)
