def solution(table, languages, preference):
    table.sort()
    a=[0,0,0,0,0]
    for i in range(len(table)):
        table[i]=list(table[i].split())
        for j in range(len(languages)):
            if languages[j] in table[i]:
                a[i]=a[i]+((6-table[i].index(languages[j]))*preference[j])
            else:
                a[i]=a[i]+0
    return table[a.index(max(a))][0]
