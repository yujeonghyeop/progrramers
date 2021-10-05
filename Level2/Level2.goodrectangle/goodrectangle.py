from math import gcd
def sero(n1,n2):
    if n1==2:
        return (2*((n2+1)//2))
    elif n1%2==0 or n2%2==0:
        return (((n1+n2)//2)*2)
    else:
         return ((((n1+n2)//2)-1)*2+1)
def solution(w,h):
    a=min(w,h)
    b=max(w,h)
    q=gcd(a,b)
    if a==1:
        return 0
    elif a==b:
        return w*h-a
    elif q==1:
        return w*h-sero(a,b)
    else:
        return w*h-q*sero(a//q,b//q)