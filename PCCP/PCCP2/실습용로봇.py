command = "LLLLLLG"
first = [0,0]
pointer = 0
dc = [1,0,-1,0]
dr = [0,1,0,-1]
for i in command:
    if pointer >=4:
        pointer=pointer%4
    elif pointer <= -4:
        pointer = pointer%4
    if i == "R":
        pointer += 1
    elif i == "L":
        pointer -= 1
    elif i == "G":
        first[0] += dr[pointer]
        first[1] += dc[pointer]
    elif i == "B":
        first[0] -= dr[pointer]
        first[1] -= dc[pointer]
print(first)