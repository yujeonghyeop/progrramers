import re
def solution(s):
    a=re.findall('[p,P]',s)
    b=re.findall('[y,Y]',s)
    return True if len(a)==len(b) else False