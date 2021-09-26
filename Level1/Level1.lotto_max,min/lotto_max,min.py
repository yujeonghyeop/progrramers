def solution(lottos, win_nums):
    s=len((set(lottos) & set(win_nums)))
    count1 = lottos.count(0)
    if s==0 and count1==0:
        answer = [6,6]
    elif s==0:
        answer = [7-(s+count1),6]
    else:
        answer = [7-(s+count1),7-s]
    return answer