def solution(brown, yellow):
    if yellow==1:
        return [3,3]
    for i in range(1,yellow//2+1):
        if yellow%i==0:
            if (brown-(i*2))//2 == (yellow//i)+2:
                return [yellow//i+2,(brown+yellow)//(yellow//i+2)]
print(solution(10,2))
print(solution(14,4))
print(solution(12,4))
print(solution(24,24))
print(solution(8,1))