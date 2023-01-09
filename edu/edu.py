#1. 이름 잘 지어라
#2. 할당 잘 해라, 파이썬은 할당이 아니라 변수를 포인팅해서 객체주소를 가리키게 한다.
#3. 요구사항 분석을 잘해라
#4. shallow copy를 조심해라, 배열을 복사 하려면 [:]를 사용하거나 deepcopy를 써야한다. 만약 2차원 배열을 복사 하려면 바깥 배열을 생성한 뒤에 for문을 돌면서 [:]로 append를 해주면 된다.

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