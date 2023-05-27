def solution(picks, minerals):
    cut = sum(picks) * 5
    minerals = minerals[0:cut]
    total = []
    cnt = 0
    answer = 0
    for i in range(len(minerals)//5 + 1):
        cnttotal = 0
        for j in range(cnt, cnt+5):
            if j >= len(minerals):
                break
            if minerals[cnt] == "diamond":
                cnttotal += 25
            elif minerals[cnt] == "iron":
                cnttotal += 5
            cnt+=1
        total.append([cnttotal,i])
    total = sorted(total,key = lambda x:x[0], reverse=True)
    for i in range(len(total)):
        cnt = total[i][1] * 5
        if picks[0] != 0:
            picks[0] -= 1
            for j in range(cnt, cnt+5):
                if j >= len(minerals):
                    break
                answer +=1
        elif picks[1] != 0:
            picks[1] -=1
            for j in range(cnt, cnt+5):
                if j >= len(minerals):
                    break
                if minerals[j] == "diamond":
                    answer +=5
                else:
                    answer +=1
        elif picks[2] !=0:
            picks[2] -= 1
            for j in range(cnt, cnt+5):
                if j >= len(minerals):
                    break
                if minerals[j] == "diamond":
                    answer +=25
                elif minerals[j] == "iron":
                    answer +=5
                else:
                    answer +=1
        else:
            break
    return answer