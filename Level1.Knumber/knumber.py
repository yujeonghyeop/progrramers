def solution(array, commands):
    answer=[]
    b=[]
    for i in range(len(commands)):  
        b.append(sorted(array[commands[i][0]-1:commands[i][1]]))
        answer.append(b[i][commands[i][2]-1])
    return answer