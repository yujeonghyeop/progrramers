def solution(n):
    b=''
    while n!=0:
        b+=str(n%3)
        n=int(n/3)
    return (int(b,3))