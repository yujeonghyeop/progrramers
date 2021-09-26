import itertools
a=[1,2,7,6,4]
answer =0
result = list(itertools.combinations(a,3))
for i in range(0,len(result)):
    b=sum(result[i])
    for j in range(2,b):
        if b%j==0:
                break
    else:
        answer+=1
print(answer)





# x = int(input())
# i=2
# while True:
#     if x%i!=0:
#         i+=1
#         if i==x:
#             print("prime!")
#             break
#     else:
#         print("not prime")
#         break