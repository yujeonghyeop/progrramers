import copy
word = 'EIO'
diction = ['A','E','I','O','U']
s = []
cnt = 0
def dfs():
    global cnt
    a=[]
    a = copy.deepcopy(s)
    if ''.join(a)==word:
        print(cnt)
        exit()
    if len(s)==5:
        return
    
    for i in range(5):
        s.append(diction[i])
        cnt+=1
        dfs()
        s.pop()
dfs()