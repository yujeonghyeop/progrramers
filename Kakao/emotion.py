from itertools import product
def solution(users, emoticons):
    answer = []
    userbuy = {}
    rate = [10,20,30,40]
    ratelist = list(product(rate,repeat = len(emoticons)))
    for i in range(len(ratelist)):
        cnt = 0
        cnt_sum = 0
        for p in range(len(users)):
            userbuy[p] = 0
        for j in range(len(ratelist[i])):
            for k in range(len(users)):
                sum = 0
                if users[k][0] <= ratelist[i][j]:
                    sum+=int(emoticons[j]-(emoticons[j]*(ratelist[i][j]/100)))
                    userbuy[k] += sum
        for k,v in userbuy.items():
            if users[k][1]<=v:
                userbuy[k] = 0
                cnt+=1
        for v in userbuy.values():
            cnt_sum +=v
        answer.append([cnt,cnt_sum])
    answer = sorted(answer, key = lambda x: (-x[0],-x[1]))
    return answer[0]