def gcd_(a,b):
    while b>0:
        a,b = b,a%b
    return a

def gcd_N(arr):
    gcd = arr[0]
    for item in arr:
        gcd = gcd_(gcd,item)
    return gcd

def solution(arrayA, arrayB):
    gcdA = gcd_N(arrayA)
    gcdB = gcd_N(arrayB)
    cnt = 0
    answer = []
    for i in arrayA:
        if i % gcdB == 0:
            break
        else:
            cnt += 1
    if cnt == len(arrayA):
        answer.append(gcdB)
    cnt =0
    for i in arrayB:
        if i % gcdA == 0:
            break
        else:
            cnt += 1
    if cnt == len(arrayB):
        answer.append(gcdA)
    if len(answer)==0:
        return 0
    else:
        answer = sorted(answer)
        return answer[-1]
