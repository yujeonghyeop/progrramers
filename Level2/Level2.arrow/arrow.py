import copy
n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]								
score= [10,9,8,7,6,5,4,3,2,1,0]
s=[]
visit = []
rion = []
answer =[0,0,0,0,0,0,0,0,0,0,0]
exception = []
def dfs(p,visit):
    print(forwin)
    if sum(s)==n:
        cnt = 0
        appeach_score = 0
        a = copy.deepcopy(info)
        for i in range(len(visit)):
            cnt+=score[visit[i]]
            a[visit[i]]=0
        for i in range(11):
            if a[i]!=0:
                appeach_score +=score[i]
        b = copy.deepcopy(visit)
        if cnt > appeach_score:
            rion.append([cnt-appeach_score,b])
        return
    for i in range(p,11):
        s.append(forwin[i])
        visit.append(i)
        dfs(i+1,visit)
        s.pop()
        visit.pop()
forwin = []
for i in range(len(info)):
    forwin.append(info[i]+1)
for i in range(info[10]):
    forwin[10] = i
    dfs(0,visit)
rion = sorted(rion,reverse=True)
if len(rion)==0:
    print(-1)
elif rion[0][0] == rion[1][0]:
    cnt = [0,0,0,0,0,0,0,0,0,0,0]
    for j in rion[0][1]:
        cnt[j] = forwin[j]
    for i in range(len(rion)):
        exanswer = [0,0,0,0,0,0,0,0,0,0,0]
        if rion[i][0] == rion[0][0]:
            for j in rion[i][1]:
                exanswer[j] = forwin[j]
        for k in range(10,-1,-1):
            if cnt[k]<exanswer[k]:
                cnt = exanswer
                break
            elif cnt[k] > exanswer[k]:
                break
else:
    for i in rion[0][1]:
        answer[i] = forwin[i]
print(answer)