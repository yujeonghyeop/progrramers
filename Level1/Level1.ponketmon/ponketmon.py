def solution(nums):
    count = int(len(nums)/2)
    nums=set(nums)
    if len(nums)<count:
        return len(nums)
    else:
        return count