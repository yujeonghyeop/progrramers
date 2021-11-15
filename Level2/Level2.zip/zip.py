def solution(msg):
    enc=    ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    i=1
    trash=''
    answer=[]
    while(msg):
        if i==(len(msg)+1):
            answer.append(enc.index(msg[:i-1])+1)
            break
        elif msg[:i] in enc:
            i+=1
        else:
            answer.append(enc.index(msg[:i-1])+1)
            trash=msg[:i-1]
            msg=msg[i-1:]
            enc.append(trash+msg[0])
            i=1
    return answer