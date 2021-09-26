def solution(a, b):
    dayname =["THU","FRI","SAT","SUN","MON","TUE","WED"]
    date =[0,31,29,31,30,31,30,31,31,30,31,30,31]
    return dayname[(sum(date[:a])+b)%7]
month1 = input()
days1 = input()
print(solution(month1,days1))