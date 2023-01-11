from collections import deque
# menu = [5, 12, 30]
# order = [2, 2, 0, 0, 0, 1, 0]	
# dq = deque()
# for i in order:
#     dq.append(i)
# k = 10
# time = 0
# cafetime = 0
# maketime = 0
# waitinglist = deque()
# cnt = 0
# maxlist = -1
# waitcount = 0
# waitinglist.append(cnt)
# while(len(dq)!=0):
#     if len(waitinglist)>maxlist:
#         maxlist = len(waitinglist)
#     print(cafetime, maketime, dq, waitinglist, cnt)
#     if cafetime+k < maketime + menu[order[cnt]]:
#         cafetime+=k
#         if waitcount < len(order)-1:
#             waitcount+=1
#             waitinglist.append(waitcount)
#     else:
#         dq.popleft()
#         if len(waitinglist) !=0:
#             waitinglist.popleft()
#         maketime += menu[order[cnt]]
#         cnt+=1
# print(maxlist)

# menu = [5,12,30]
# order = [2, 2, 0, 0, 0, 1, 0]
# k = 10
# time = 0
# maxwaitng = -1
# for i in range(len(order)):
#     time += menu[order[i]]
#     if time%k ==0:
#         waiting = (time//k)  - (i)
#     else:
#         waiting = (time//k) +1 - (i)
#     if waiting >= maxwaitng:
#         maxwaitng = waiting
# print(maxwaitng)

menu = [5,12,30]
order = [1,2,0,1]
k = 10
dq = deque()
waiting = deque()
maketime = 0
answer = 0
for i in range(k*(len(order)-1)+1):
    if len(waiting) != 0:
        if i == maketime + menu[order[waiting[0]]]:
            maketime +=menu[order[waiting[0]]]
            waiting.popleft()
    if i % k ==0:
        waiting.append(i//k)
    answer = max(answer, len(waiting))  
print(answer)
