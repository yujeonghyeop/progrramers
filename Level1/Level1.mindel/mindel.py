def solution(arr):
    arr.remove(sorted(arr,key=lambda x:x,reverse=True).pop())
    return [-1] if len(arr)==0 else arr
