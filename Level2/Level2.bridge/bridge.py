import collections


def solution(bridge_length, weight, truck_weights):
    answer = 1
    cnt = collections.deque(truck_weights)
    bridge = collections.deque([0]*bridge_length)
    bridge[-1] = cnt.popleft()
    sum = bridge[-1]
    while(len(bridge) != 0):
        sum -= bridge[0]
        bridge.popleft()
        if len(cnt) != 0:
            if sum+cnt[0] > weight:
                bridge.append(0)
            else:
                bridge.append(cnt.popleft())
                sum += bridge[-1]
        answer += 1
    return answer
