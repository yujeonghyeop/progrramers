def solution(a, b):
    dayname =["THU","FRI","SAT","SUN","MON","TUE","WED"]
    date =[0,31,29,31,30,31,30,31,31,30,31,30,31]
    sum = 0
    a=int(a)
    b=int(b)
    for i in range(0,a):
        sum = date[i]+sum
    answer = dayname[(sum+b)%7]
    return answer

month1 = input()
days1 = input()
print(solution(month1,days1))