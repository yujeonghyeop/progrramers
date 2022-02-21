import math
fees = [1, 461, 1, 10]#기본시간, 기본요금, 단ㅜ위 시간, 단위 요금
records = ["00:00 1234 IN"]
time = {}
rtime = {}
answer = []
for i in range(len(records)):
    records[i] = records[i].split(' ')
for i in range(len(records)):
    records[i][0] = (int(records[i][0][0:2])*60 + int(records[i][0][3:5]))
for i in range(len(records)):
    if records[i][2]=="IN":
        time[records[i][1]] = records[i][0]
    elif records[i][2] == "OUT":
        if records[i][1] in rtime:
            rtime[records[i][1]]  += (records[i][0] - time[records[i][1]])
            time[records[i][1]] =-1
        else:
            rtime[records[i][1]] = records[i][0] - time[records[i][1]]
            time[records[i][1]] =-1
for i in time.items():
    if i[1] !=-1:
        if i[0] in rtime:
            rtime[i[0]] += (1439 - int(i[1]))
        else:
            rtime[i[0]] = (1439 - int(i[1]))
for i in rtime.items():
    if i[1] <= fees[0]:
        rtime[i[0]] = fees[1]
    else:
        rtime[i[0]] = fees[1] + (math.ceil((i[1] - fees[0])/fees[2])) * fees[3]
rtime = sorted(rtime.items(), key = lambda x:x[0])
for i in rtime:
    answer.append(i)
print(answer)
