def solution(id_list, report, k):
    report = list(set(report))
    cnt = {}
    cnt1= {}
    for i in id_list:
        cnt1[i] = 0
    for i in range(len(report)):
        report[i] = report[i].split()
    for j in range(len(report)):
        if report[j][1] not in cnt:
            cnt[report[j][1]]=1
        else:
            cnt[report[j][1]]+=1
    for p in range(len(report)):
        if cnt[report[p][1]] >= k:
            cnt1[report[p][0]]+=1
    return list(cnt1.values())
