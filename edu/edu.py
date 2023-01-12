#1. 이름 잘 지어라
#2. 할당 잘 해라, 파이썬은 할당이 아니라 변수를 포인팅해서 객체주소를 가리키게 한다.
#3. 요구사항 분석을 잘해라
#4. shallow copy를 조심해라, 배열을 복사 하려면 [:]를 사용하거나 deepcopy를 써야한다. 만약 2차원 배열을 복사 하려면 바깥 배열을 생성한 뒤에 for문을 돌면서 [:]로 append를 해주면 된다.
#5. String
#6. Bit mask(부분집합 찾기)
#7. 2차원 리스트, zip을 활용해서 전치를 해줄 수 있다(행렬 바꾸기)
#       matrix = [[3,7,9],[4,2,6],[8,1,5]]
#       zipped_matrix = list(map(list,zip(*matrix)))
#       print(zipped_matrix)
#8. dfs - 구조화(인접 행렬, 인접 리스트), 풀이방법(스택, 재귀) --> 4가지 방식의 풀이 가능(인접행렬, 스택 조합을 추천)
# 파트1. Hashing
# def solution(id_list, report, k):
#     newreport = list(set(report))
#     warn = {}
#     result = {}
#     for i in id_list:
#         warn[i] = 0
#         result[i] = 0
#     for i in newreport:
#         splitrepor = i.split()
#         warn[splitrepor[1]] +=1
#     for j in newreport:
#         splitrepor = j.split()
#         if(warn[splitrepor[1]]>=k):
#             result[splitrepor[0]] += 1
#     return list(result.values())

#1일차 모의고사 1번
# show = {"zero" : 0, "one" : 1, "two" : 2, "three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
# s = "one4seveneight"
# answer = ""
# temp = ""
# for i in range(len(s)):
#     if s[i].isdigit() == True:
#         answer+=s[i]
#     else:
#         temp +=s[i]
#         if temp in show.keys():
#             answer += str(show[temp])
#             temp = ''
# print(answer)

#1일차 모의고사 2번
# my_string = "We are the world"	
# check = {}
# result = ""
# for i in my_string:
#     check[i] = 0
# for j in my_string:
#     check[j] +=1
#     if check[j] == 1:
#         result += j
# print(result)

#1일차 모의고사 3번
# s = "abcabcadc"	
# check = {}
# answer = ""
# for i in s:
#     if i in check:
#         check[i] +=1
#     else:
#         check[i] = 1
# for k, v in check.items():
#     if v == 1:
#         answer += k
# answer = ''.join(sorted(answer))
# print(answer)

#파트2 array 구현력
# import math
# fees = [180, 5000, 10, 600]
# records = [
#     "05:34 5961 IN", 
#     "06:00 0000 IN", 
#     "06:34 0000 OUT", 
#     "07:59 5961 OUT", 
#     "07:59 0148 IN", 
#     "18:59 0000 IN", 
#     "19:09 0148 OUT", 
#     "22:59 5961 IN", 
#     "23:00 5961 OUT"]
# answer = []
# status = {}
# time = {}
# for i in records:
#     info = i.split()
#     if info[2] == "IN":
#         status[info[1]] = info[0]
#     elif info[2] == "OUT":
#         enter = int(status[info[1]][0:2]) * 60 + int(status[info[1]][3:5]) 
#         out = int(info[0][0:2]) * 60 + int(info[0][3:5]) 
#         temptime = out - enter
#         status.pop(info[1])
#         if info[1] in time:
#             time[info[1]] += temptime
#         else:
#             time[info[1]]= temptime
# for k,v in status.items():
#     enter = int(v[0:2])*60 + int(v[3:5])
#     out = 1439
#     if k in time:
#         time[k] += (out-enter)
#     else:
#         time[k] = out-enter
# time = sorted(time.items(), key = lambda x:x[0])
# for i in time:
#     if i[1]< fees[0]:
#         answer.append(fees[1])
#     else:
#         sumfee = fees[1] + math.ceil((i[1]-fees[0])/fees[2]) * fees[3]
#         answer.append(int(sumfee))
# print(answer)

# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# setgems = list(set(gems))
# status = False
# answer = []
# left = 0
# right = len(gems) -1 
# while(left <= right):
#     temparr = list(set(gems[left:right+1]))
#     if sorted(temparr) == sorted(setgems):
#         answer.append([left+1,right+1])
#         right -= 1
#         status = True
#     else:
#         if status == True:
#             right += 1
#         left += 1
#         status = False
# answer = sorted(answer, key = lambda x: x[0])
# sortedanswer = sorted(answer, key = lambda x : x[1]-x[0])
# print(sortedanswer, sortedanswer[0])


# answer = 0
# def dfs(k, dungeon, cnt, visited):
#     global answer
#     if cnt > answer:
#         answer = cnt
#     for i in range(len(dungeon)):
#         if visited[i] == 0 and dungeon[i][0] <= k:
#             visited[i] = 1
#             dfs(k-dungeon[i][1], dungeon,cnt +1,visited)
#             visited[i] = 0
# def solution(k, dungeons):
#     visited = [0] * len(dungeons)
#     dungeons = sorted(dungeons, key = lambda x:x[0])
#     dfs(k, dungeons,0, visited)
#     return answer

# def solution(routes):
#     routes = sorted(routes, key = lambda x:x[1])
#     camera = -300001
#     cnt = 0
#     for i in range(len(routes)):
#         if camera >= routes[i][0] and camera <= routes[i][1]:
#             continue
#         else:
#             camera = routes[i][1]
#         cnt+=1
#     return cnt
# import sys
# n = int(input())
# answer = []
# def swimming(credit, plan):
#     for i in range(len(plan)):
        
# for i in range(n):
#     credit = []
#     plan = []
#     credit = list(map(int, sys.stdin.readline().split()))
#     plan = list(map(int, sys.stdin.readline().split()))
#     swimming(credit, plan)


s=5
e=16
result = 0
while(s!=e):
    print(s)
    if (s>e):
        result = s-e
        print(s,result)
        break
    elif e-s >= 5:
        s+=5
        result += 1
        print("5칸이동",s,result)
    elif (e-s)==4:
        s+=4
        result +=2
        print("2칸이동",s,result)        
    else:
        s+= (e-s)
        result += (e-s)
        print("차 이동",e-s,s,result)
print(result)
