def solution(genres, plays):
    song = {}
    answer = []
    for i in range(len(genres)):
        if genres[i] in song:
            song[genres[i]] += plays[i]
        else:
            song[genres[i]] = plays[i]
    song = sorted(song.items(), key = lambda x:x[1],reverse=True)
    for i in range(len(song)):
        cnt = []
        for j in range(len(genres)):
            if genres[j] == song[i][0]:
                cnt.append([plays[j],j])
        cnt = sorted(cnt, key = lambda x:x[0],reverse=True)
        for k in range(len(cnt)):
            if k == 2:
                break
            else:
                answer.append(cnt[k][1])
    return answer