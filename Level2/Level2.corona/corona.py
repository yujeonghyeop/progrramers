def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solution(places):
    cnt=[]
    answer=[1,1,1,1,1]
    for i in range(len(places)):
        cnt=[]
        for j in range(5):
            for k in range(5):
                if places[i][j][k]=='P':
                    c=[j,k]
                    cnt.append([j,k])
                    if len(cnt)!=1:
                        for p in range(len(cnt)-1):
                            if manhattan(cnt[p],c)<=2:
                                if manhattan(cnt[p],c)==1:
                                    answer[i]=0
                                    break
                                elif manhattan(cnt[p],c)==2 and cnt[p][0]!=c[0] and cnt[p][1]!=c[1]:
                                    if places[i][cnt[p][0]][c[1]] =='O' or  places[i][c[0]][cnt[p][1]]=='O':
                                        answer[i]=0
                                        break
                                else:
                                    if places[i][(cnt[p][0]+c[0])//2][(cnt[p][1]+c[1])//2]=='O':
                                        answer[i]=0
                                        break
    return answer
