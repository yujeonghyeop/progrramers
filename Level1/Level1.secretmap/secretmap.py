def solution(n, arr1, arr2):
    arr3=[]
    answer=[]
    for i in range(n):
        arr3.append(((bin(arr1[i]|arr2[i])[2:])))
        if len(arr3[i])<n:
            arr3[i]=arr3[i].zfill(n)
        arr3[i]=(arr3[i].replace('0'," "))
        answer.append(arr3[i].replace('1','#'))
    return answer