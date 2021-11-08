def solution(n):
    answer = 0
    i=n+1
    while(True):
        if bin(i).count("1")==bin(n).count("1"):
            answer=i
            break
        else:
            i+=1
    return answer
