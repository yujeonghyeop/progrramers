def solution(a, b):
    return (max(a,b)*(max(a,b)+1))//2-((min(a,b)-1)*min(a,b))//2