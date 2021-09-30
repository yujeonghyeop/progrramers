def solution(scores):
    answer = ''
    scores=list(map(list,zip(*scores)))
    for i in range(len(scores)):
        cnt=len(scores)
        if max(scores[i])==scores[i][i] or min(scores[i])==scores[i][i]:
            if scores[i].count(scores[i][i])==1:
                scores[i][i]=0
                cnt-=1
        if sum(scores[i])/cnt>=90:
            answer+='A'
        elif 80<=sum(scores[i])/cnt<90:
            answer+='B'
        elif 70<=sum(scores[i])/cnt<80:
            answer+='C'
        elif 50<=sum(scores[i])/cnt<70:
            answer+='D'
        else:
            answer+='F'
    return answer