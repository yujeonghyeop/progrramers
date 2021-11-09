def change(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    return change(q, base) + T[r] if q else T[r]

def solution(n, t, m, p):
    cnt=''
    answer=''
    for i in range(t*m):
        cnt+=(change(i,n))
    cnt=list(cnt)
    for j in range(p-1,t*m,m):
        answer+=cnt[j]
    return answer
    