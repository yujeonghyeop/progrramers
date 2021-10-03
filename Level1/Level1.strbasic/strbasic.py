import re
def solution(s):
    a=''.join(re.findall('\d',s))
    return True if (len(s)==4 or len(s)==6) and a==s else False