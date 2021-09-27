def solution(weights, head2head):
    answer = []
    merit=[]
    rate=[]
    a=[]
    for i in range(len(weights)):
        m_cnt=0
        w_cnt=0
        l_cnt=0
        for j in range(len(weights)):
            if head2head[i][j]=="W":
                w_cnt+=1
                if weights[i]<weights[j]:
                    m_cnt+=1
            elif head2head[i][j]=="L":
                l_cnt+=1
        if w_cnt+l_cnt==0:
            rate.insert(i,0)
        else:
            rate.insert(i,w_cnt/(w_cnt+l_cnt))
        merit.insert(i,m_cnt)
    for i in range(len(weights)):
        a.append({"index":i,"weight":weights[i],"win":rate[i],"merit":merit[i]})
    a.sort(key=lambda x: x["weight"],reverse=True)
    a.sort(key=lambda x: x["merit"],reverse=True)
    a.sort(key=lambda x: x["win"],reverse=True)
    return [i["index"]+1 for i in a]