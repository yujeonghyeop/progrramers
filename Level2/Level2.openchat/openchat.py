def solution(record):
    answer = []
    answer=[]
    new1=" ".join(record)
    new=new1.split()
    inf={}
    for i in range(len(new)):
        if new[i]=='Enter' or new[i]=='Change':
            inf[new[i+1]]=new[i+2]
    for i in range(len(new)):
        if new[i]=='Enter':
            answer.append("{}님이 들어왔습니다.".format(inf[new[i+1]]))
        elif new[i]=='Leave':
            answer.append("{}님이 나갔습니다.".format(inf[new[i+1]]))
    return answer