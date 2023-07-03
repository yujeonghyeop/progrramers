def solution(players, callings):
    playerdict = {}
    rankdict = {}
    answer = []
    for i in range(len(players)) :
        playerdict[players[i]]=i+1
        rankdict[i+1] = players[i]
    for j in callings:
        playerdict[j] -= 1
        playerdict[rankdict[playerdict[j]]] +=1
        rankdict[playerdict[j]], rankdict[playerdict[j]+1] = j,rankdict[playerdict[j]]

    playerdict =sorted(playerdict.items(), key = lambda x: x[1])
    playerdict = list(playerdict)
    for k in playerdict:
        answer.append(k[0])
    return answer
