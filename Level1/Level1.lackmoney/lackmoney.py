def solution(price, money, count):
    if sum(price*i for i in range(1,count+1))-money<0:
        return 0
    else:
        return sum(price*i for i in range(1,count+1))-money