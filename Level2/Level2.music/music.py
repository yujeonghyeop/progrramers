def solution(m, musicinfos):
    m=m.replace('C#','c').replace('D#','d').replace('F#','f').replace('A#','a').replace('G#','g').replace('E#','e')
    time=[]
    cnt=''
    count=0
    music=[]
    answer=[]
    maxtime={}
    for i in range(len(musicinfos)):
        musicinfos[i]=musicinfos[i].split(',')
        musicinfos[i][3]=musicinfos[i][3].replace('C#','c').replace('D#','d').replace('F#','f').replace('A#','a').replace('G#','g').replace('E#','e')
    for i in range(len(musicinfos)):
        for j in range(2):
            musicinfos[i][j]=musicinfos[i][j].split(':')
    for i in range(len(musicinfos)):
        time.append((int(musicinfos[i][1][0])*60+int(musicinfos[i][1][1]))-(int(musicinfos[i][0][0])*60+int(musicinfos[i][0][1])))
        for j in range(time[i]):
            cnt+=musicinfos[i][3][j%len(musicinfos[i][3])]
        music.append(cnt)
        cnt=''
    for i in music:
        if m in i:
            answer.append(count)
            count+=1
        else:
            count+=1
    if len(answer)>=2:
        for i in range(len(answer)):
            maxtime[answer[i]]=(time[answer[i]])
        new_dict = sorted(maxtime.items(), key=lambda x:x[1], reverse=True)
        return musicinfos[new_dict[0][0]][2]
    elif len(answer)==1:
        return musicinfos[answer[0]][2]
    elif len(answer)==0:
        return "(None)"