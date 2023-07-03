def solution(picks, minerals):
    cut = sum(picks) * 5    ##곡괭이의 갯수 *5 뒤에 있는 광물들은 어짜피 못캐므로 처음부터 짤라버린다.
    minerals = minerals[0:cut] ##처음부터 자름
    total = []
    cnt = 0
    answer = 0
    for i in range(len(minerals)//5 + 1):   ##5로 잘라서 계산했을 때 해당 범위의 광물 중요도를 계산해주는 반복문
        cnttotal = 0
        for j in range(cnt, cnt+5):
            if j >= len(minerals):
                break
            if minerals[cnt] == "diamond":  ##해당 광물이 다이아몬드라면 +25
                cnttotal += 25
            elif minerals[cnt] == "iron":   ##해당 광물이 철이라면 +5, 돌이라면  굳이 안해줘도 됨
                cnttotal += 5
            cnt+=1
        total.append([cnttotal,i])  ##비교해주기 위해 배열에 추가
    total = sorted(total,key = lambda x:x[0], reverse=True) ##가장 우선순위가 높은 범위를 제일 좋은 곡괭이를 사용해야 하기 때문에 역정렬
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