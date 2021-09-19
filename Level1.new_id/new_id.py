import re
def solution(new_id): #1단계
    answer =''
    second = re.sub(r'[^a-z0-9-._]',"",new_id.lower())
    third = re.sub('[.]{2,}','.',second)
    answer = third.strip("[.]")
    if len(answer)==0:
        answer ='aaa'
    while len(answer)<3:
            answer += answer[-1]
    if len(answer)>=16:
        answer=answer[:15]
        answer = answer.strip("[.]")
    return answer
a= input()
print(solution(a))