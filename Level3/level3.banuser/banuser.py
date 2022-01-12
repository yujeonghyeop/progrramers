def solution(user_id, banned_id):
    cnt = [[]]
    answer=[]
    for j in range(len(banned_id)):
        new=[]
        for i in range(len(user_id)):
            if len(user_id[i])==len(banned_id[j]):
                cnt1 = True
                for p in range(len(banned_id[j])):
                    if banned_id[j][p]=='*':
                        continue
                    elif banned_id[j][p]==user_id[i][p]:
                        continue
                    else:
                        cnt1 = False
                        break
                if cnt1 == True:
                    for c in cnt:
                        if user_id[i] not in c:
                            new.append(c+[user_id[i]])
            else:
                continue
        cnt = new
    for c in cnt:
        if set(c) not in answer:
            answer.append(set(c))
    return len(answer)