#1. 이름 잘 지어라
#2. 할당 잘 해라, 파이썬은 할당이 아니라 변수를 포인팅해서 객체주소를 가리키게 한다.
#3. 요구사항 분석을 잘해라

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

