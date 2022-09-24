import time
def solution(today, terms, privacies):
    first = time.strptime(today,"%Y.%m.%d")
    answer = []
    term = {}
    for i in range(len(terms)):
        term[terms[i][0]] = terms[i][2:]
    for i in range(len(privacies)):
        left = int(term[privacies[i][11]])
        year = int(privacies[i][0:4])
        month = int(privacies[i][5:7])
        date = int(privacies[i][8:10])
        aftermonth = left + month
        if aftermonth%12!=0:
            month = aftermonth%12
            year += aftermonth//12
        else:
            month =12
            year += aftermonth//12-1
        stryear = str(year) +"/"+ str(month) +"/"+ str(date)
        second = time.strptime(stryear,"%Y/%m/%d")
        if second<=first:
            answer.append(i+1)
    return answer