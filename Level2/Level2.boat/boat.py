def solution(people, limit):
    answer =0
    cnt=0
    people.sort()
    people.reverse()
    i=0
    j=len(people)-1
    while(i<j):
        if people[i]+people[j]<=limit:
            answer+=1
            people[i]=0
            people[j]=0
            i+=1
            j-=1
        else:
            people[i]=0
            i+=1
            answer+=1
    if sum(people)!=0:
        answer+=1
    return answer