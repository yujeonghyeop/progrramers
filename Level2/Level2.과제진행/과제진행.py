from collections import deque

def solution(plans):
    doingwork = deque()
    willwork = deque()
    donework = []
    answer = []
    sumtime = 0

    for i in  plans:
        i[1] = int(i[1][0:2]) * 60 + int(i[1][3:5])
        i[2] = int(i[2])
        sumtime += i[2]

    plans = sorted(plans, key=lambda x:x[1])


    plans = deque(plans)
    mintime = plans[0][1]
    maxtime = plans[-1][1]

    doingwork.append(plans.popleft())

# , 
# ["music", "740", "40"],
# "computer", "750", "100"]]
#[["science", "760", "50"]
# ["history", "840", "30"]

    for j in range(mintime,maxtime + sumtime+1):
        if len(plans) != 0:
            if j == plans[0][1]:
                if len(doingwork) !=0:
                    willwork.append(doingwork.popleft())
                doingwork.append(plans.popleft())
        if len(doingwork)!= 0:
            doingwork[0][2] -= 1    
            if doingwork[0][2] == 0:
                donework.append(doingwork.popleft())
                if len(willwork) !=0:
                    doingwork.append(willwork.pop())
    for p in donework:
        answer.append(p[0])
    return answer
