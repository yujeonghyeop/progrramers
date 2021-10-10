def solution(s):
    s=list(s.lower())
    i=0
    while i<len(s):
        if s[i]==' ':
            i+=1
            continue
        s[i]=s[i].upper()
        i+=2
    return ''.join(s)