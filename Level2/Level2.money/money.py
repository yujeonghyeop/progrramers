# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]
#prices = {1, 2, 3, 2, 3, 1} return {5, 4, 1, 2, 1, 0}

prices=[1,2,3,2,3,1]
answer=[]
cnt=0
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        if prices[i]<=prices[j]:
            cnt+=1
        else:
            cnt+=1
            break
    answer.append(cnt)
    cnt=0
print(answer)
