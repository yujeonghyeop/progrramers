def solution(s, skip, index):
    answer = ''
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet = sorted(list(set(alphabet) - set(list(skip))))
    for i in range(len(s)):
        change = (alphabet.index(s[i])+index) % len(alphabet)
        answer += alphabet[change]
    return answer