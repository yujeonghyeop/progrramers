import math
def solution(n,a,b):
    answer=1
    while(True):
        if abs(b-a)==1 and math.ceil(a/2)==math.ceil(b/2):
            return answer
        else:
            a=math.ceil(a/2)
            b=math.ceil(b/2)
            answer+=1
