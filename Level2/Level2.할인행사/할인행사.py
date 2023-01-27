def solution(want, number, discount):
    dic = {}
    result = 0
    for i in range(len(want)):
        dic[want[i]] = number[i]
    for i in range(len(discount)-9):
        cntdic = {}
        cntdiscount = discount[i:i+10]
        for j in cntdiscount:
            if j not in cntdic:
                cntdic[j] = 1
            else:
                cntdic[j] +=1
        if dic == cntdic:
            result +=1
    return result