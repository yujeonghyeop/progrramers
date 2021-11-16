def solution(dlrs):
    x,y,nx,ny=0,0,0,0
    stack=set()
    answer=0
    for i in range(len(dlrs)):
        if dlrs[i]=="U":
            x+=1
        elif dlrs[i]=="D":
            x-=1
        elif dlrs[i]=="L":
            y-=1
        elif dlrs[i]=="R":
            y+=1
        if abs(x)>5 or abs(y)>5:
            x,y=nx,ny
            continue
        if (nx,ny,x,y) not in stack:
            stack.add((x,y,nx,ny))
            stack.add((nx,ny,x,y))
            answer+=1
        nx,ny=x,y
    return answer