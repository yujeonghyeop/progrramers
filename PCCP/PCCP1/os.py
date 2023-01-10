from queue import PriorityQueue

def solution(program):
    pq = PriorityQueue()
    program = sorted(program, key = lambda x :x[1])
    cur = 0
    answer = [0] * 10
    def call_program():
        while(len(program) > 0) and program[0][1] <= cur:
            pq.put(program.pop(0))
    while(len(program)>0 or not pq.empty()):
        if pq.empty():
            cur = program[0][1]
            call_program()
        execute = pq.get()
        answer[execute[0]-1] += cur - execute[1]
        cur += execute[2]
        call_program()
    return [cur] + answer