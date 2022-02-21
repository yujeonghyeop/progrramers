board = [
        [5,5,5,5,5],
        [5,5,5,5,5],
        [5,5,5,5,5],
        [5,5,5,5,5]
        ]
skill = [
    [1,0,0,3,4,4],
    [1,2,0,2,3,2],
    [2,1,0,3,1,2],
    [1,0,1,3,3,1]
    ]
answer =0
for i in range(len(skill)):
    if skill[i][0] == 1:
        for j in range(skill[i][1],skill[i][3]+1):
            for k in range(skill[i][2],skill[i][4]+1):
                board[j][k] -= skill[i][5]
    elif skill[i][0] ==2:
        for j in range(skill[i][1],skill[i][3]+1):
            for k in range(skill[i][2],skill[i][4]+1):
                board[j][k] += skill[i][5]

for i in range(len(board)):
    for j in range(len(board[1])):
        if board[i][j] > 0:
            answer +=1
print(answer)