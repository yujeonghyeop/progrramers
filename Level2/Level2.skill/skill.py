def solution(skill, skill_trees):
    answer =0
    skill=list(skill)
    for i in range(len(skill_trees)):
        stack=list(skill_trees[i])
        k=0
        for j in range(len(stack)):
            if stack[j] in skill:
                if stack[j]==skill[k]:
                    k=k+1
                else:
                    break
            if j==len(stack)-1:
                answer+=1
    return answer