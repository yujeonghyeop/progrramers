import itertools
def solution(orders, course):
    answer=[]
    orders=sorted(orders)
    for k in course:
        cnt={}
        ans=[]
        for i in range(len(orders)):
            a=itertools.combinations(sorted(orders[i]),k)
            a=list(a)
            for j in range(len(a)):
                if a[j] in cnt:
                    cnt[a[j]]+=1
                else:
                    cnt[a[j]]=1
        new_dict = sorted(cnt.items(), key=lambda x:x[1], reverse=True)
        if new_dict[0][1]==1:
            continue
        else:
            for key, value in cnt.items():
                if new_dict[0][1] == value:
                    ans.append(key)
            for l in range(len(ans)):
                answer.append(''.join(ans[l]))
    return sorted(answer)