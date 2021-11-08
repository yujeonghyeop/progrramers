def solution(s):
    s=s.lower() #일단 모든 문자를 소문자로 변환해준다
    for i in range(len(s)): 
        if s[i]==' ':   #s의 길이만큼 포문을 돌면서 공백이 나오면 그 뒤의 문자를 대문자로 바꾸기 위해 if문을 사용한다.
            if i==len(s)-1: #만약 i가 s문자열의 끝에서 -1이라면 뒤에 바꿀 문자가 없기 때문에 그냥 진행시켜준다.
                break
            else:
                s=s[:i+1]+s[i+1].upper()+s[i+2:]    #문자열은 삭제가 되지 않기 때문에 슬라이싱으로 공백까지의 문자열과 공백다음의문자열을 대문자로바꾼것, 공백 뒤의 문자열을 합쳐준다.
        elif i==0:  #i가 0이고, 공백이 아니라면 
            s=s[:i]+s[i].upper()+s[i+1:]    #바로 문자열을 upper해준다.
    return s