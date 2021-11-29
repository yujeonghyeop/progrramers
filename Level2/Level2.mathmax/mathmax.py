import copy
def solution(expression):
    number = [["+", "-", "*"], ["+", "*", "-"], ["*", "+", "-"],
        ["*", "-", "+"], ["-", "*", "+"], ["-", "+", "*"]]
    a = []
    b = []
    cnt = 0
    c = []
    d = []
    k = 0
    max = 0
    for i in range(len(expression)):
        if expression[i].isdigit() != True:
            a.append(expression[i])
            b.append(expression[cnt:i])
            cnt = i+1
    b.append(expression[cnt:])
    for i in range(len(number)):
        c = copy.deepcopy(a)
        d = copy.deepcopy(b)
        for j in range(len(a)):
            if number[i][0] in c:
                k = c.index(number[i][0])
                d[k] = str(eval(d[k]+number[i][0]+d[k+1]))
                del c[k]
                del d[k+1]
            elif number[i][0] not in c and number[i][1] in c:
                k = c.index(number[i][1])
                d[k] = str(eval(d[k]+number[i][1]+d[k+1]))
                del c[k]
                del d[k+1]
            elif number[i][0] not in c and number[i][1] not in c and number[i][2] in c:
                k = c.index(number[i][2])
                d[k]=str(eval(d[k]+number[i][2]+d[k+1]))
                del c[k]
                del d[k+1]
        if abs(int(d[0])) >= max:
            max=abs(int(d[0]))
    return max
