def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    cnt1=[]
    cnt2=[]
    n=0
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            cnt1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            cnt2.append(str2[i:i+2])
    for i in cnt1:
        if i in cnt2:
            cnt2[cnt2.index(i)]=0
            n+=1
    u=len(cnt1)+len(cnt2)-n
    return int((n/u)*65536) if u!=0 else 65536