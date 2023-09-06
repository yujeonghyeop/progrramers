def solution(alp, cop, problems):
    answer = 0
    alp_max = 0
    cop_max = 0
    for i in problems:  ##Dp의 최댓값을 지정해주기 위해 각각의 최댓값을 구한다
        alp_max = max(i[0], alp_max)
        cop_max = max(i[1], cop_max)
    alp = min(alp, alp_max) ## 최댓값 넘으면 안되기 때문에 min 세팅
    cop = min(cop, cop_max)
    INF = float('inf')
    dp = [[INF]*(cop_max + 1)  for _ in range(alp_max + 1)] ##dp의 의미는 알고력 i, 코딩력 j에 다르기까지 걸리는 시간이다.
    dp[alp][cop]=0
    for i in range(alp,alp_max + 1):
        for j in range(cop, cop_max+1):
            if i < alp_max:
                dp[i+1][j] = min(dp[i][j] + 1, dp[i+1][j])  ##단순히 이전값에서 1초더있으면 알고력이 추가됨
            if j < cop_max:
                dp[i][j+1] = min(dp[i][j] +1, dp[i][j+1])   ## 단순히 이전값에서 1초 더있으면 코딩력이 추가됨
            for a, c, ax, cx, time in problems:
                if i>=a and j >=c:
                    new_alp = min(i + ax, alp_max)
                    new_cop = min(j + cx, cop_max)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop],dp[i][j] + time)    ## 문제를 풀면서 추가되는 알고력, 코딩력에 시간과 비교하여 dp 업데이트
    return dp[-1][-1]