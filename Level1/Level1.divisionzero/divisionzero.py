def solution(arr, divisor):
    arr=sorted(arr)
    answer=[]
    for i in arr:
        if int(i)%divisor==0:
            answer.append(i)
    return [-1] if answer==[] else answer