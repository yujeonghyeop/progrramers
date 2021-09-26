def solution(N, stages):
    a=[]
    b={}
    for i in range(N+2):
        a.append(stages.count(i))
    for i in range(1,N+1):
        if sum(a[i:])!=0:
            b[i]=(a[i]/sum(a[i:]))
        else: 
            b[i]=(0)
    return sorted(b,key=lambda x:b[x],reverse=True)