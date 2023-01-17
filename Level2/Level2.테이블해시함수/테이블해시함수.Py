def solution(data, col, row_begin, row_end):
    cnt = []
    data = sorted(data, key = lambda x:[x[col-1],-x[0]])
    cal=0
    for i in range(row_begin-1, row_end):
        cal = 0
        for j in range(len(data[i])):
            cal += data[i][j]%(i+1)
        cnt.append(cal)
    answer = cnt[0]
    for i in range(1, len(cnt)):
        answer = answer ^ cnt[i]
    return answer