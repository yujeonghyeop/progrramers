def solution(sizes):
    max_0=0
    max_1=0
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]:
            sizes[i].reverse()
        if sizes[i][0]>max_0:
            max_0=sizes[i][0]
        if sizes[i][1]>max_1:
            max_1=sizes[i][1]
    return(max_0*max_1)