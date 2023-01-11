import sys
n = int(input())
for i in range(n):
    m = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    answer = max(arr) - min(arr)
    print("#{} {}".format(i+1, answer))