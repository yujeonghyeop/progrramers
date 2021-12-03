def cal(name):
    answer=0
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    beta = [0, 'Z', 'Y', 'X', 'W', 'V', 'U', 'T', 'S', 'R', 'Q', 'P', 'O', 'N']
    for i in range(len(name)):
        if name[i] != 'A':
            if name[i] in alpha:
                answer += alpha.index(name[i])
            else:
                answer += beta.index(name[i])
        if sum(ord(ch) for ch in name[i+1:])==(len(name)-i-1)*65:
            print(name[i+1:],i)
            return answer
        if i!=len(name)-1:
            answer+=1
    return answer
name = 'ABAAAAAAAAABB'
name1=''
name2=''

if len(name)%2==0:
    name1=name[:len(name)//2]
    name2=name[len(name)//2:]
else:
    name1=name[:len(name)//2]
    name2=name[len(name)//2:]
    name2=name2[::-1]
print(name1,name2)
print(cal(name1),cal(name2))
print(cal(name1)+cal(name2)+1)
