def solution(n, words):
    answer=[0,0]
    stack =[]
    for i in range(len(words)):
        if words[i] in stack:
            answer[0]=i%n+1
            answer[1]=i//n+1
            break
        elif i!=len(words)-1 and words[i][-1] != words[i+1][0]:
            answer[0]=(i+1)%n+1
            answer[1]=(i+1)//n+1
            break
        else:
            stack.append(words[i])
    return answer