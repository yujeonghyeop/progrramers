# import re
# def solution(phone_book):
#     answer = True
#     p=re.compile(phone_book[0])
#     for i in range(1,len(phone_book)):
#         m=p.match(phone_book[i])
#         if m:
#             answer=False
#     return answer
import re
answer=True
person={}
phone_book=["12","123","1235","567","88"]
person={}
for i in range(len(phone_book)):
    person={i:phone_book[i]}
print(person)