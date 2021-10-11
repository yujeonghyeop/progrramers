import math
def solution(n, m):
    a=math.gcd(n,m)
    return a,a*(n//a)*(m//a)