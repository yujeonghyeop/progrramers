def solution(participant, completion):
    p=sorted(participant)
    c=sorted(completion)
    c.append("")
    for i in range(0,len(c)):
        if p[i]!=c[i]:
            return p[i]