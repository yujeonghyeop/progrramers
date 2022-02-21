import string
import math
n = 1000000
k = 10
tmp = string.digits+string.ascii_uppercase
def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]

def primenumber(b):
    for i in range(2, int(math.sqrt(b))+1):
        if b % i == 0:
            return False 
    return True 
num = (convert(n,k))
print(num)
cnt = []
answer =[]
j = 0
for i in range(len(num)):
    if num[i]=='0' and num[j:i] != '':
        cnt.append(int(num[j:i]))
        j = i+1
print(j)
if j!=len(str(num)):
    cnt.append(int(num[j:]))
for i in cnt:
    if i==2:
        answer.append(i)
    elif i!=1:
        if primenumber(i)==True:
            answer.append(i)

print(len(answer))