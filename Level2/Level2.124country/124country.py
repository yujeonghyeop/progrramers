def solution(n):
    a='412'
    answer=''
    cnt=0
    i=0
    while n>cnt:
        i+=1
        cnt+=3**i
    for j in range(i):
        answer+=a[n%3]
        if n%3==0:
            n=n//3-1
        else:
            n=n//3
    return answer[::-1]