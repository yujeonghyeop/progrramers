import heapq

def dijkstra(graphA, graphB,transfer, start, N):
    INF = int(1e9)
    distances = [(INF,-1,0)] * (N + 1)
    distances[start] = (0,-1,0)

    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)
        tmp = 0
        if distances[node][0] < dist:
            continue
        for neighbor, weight in graphA[node]:
            cost = dist + weight
            if cost < distances[neighbor][0]:
                if distances[node][1] == 'B':
                    tmp = distances[node][2] + transfer[node-1]
                else:
                    tmp = distances[node][2]
                distances[neighbor] = (cost,'A',tmp)
                heapq.heappush(q, (cost, neighbor))
        for neighbor, weight in graphB[node]:
            cost = dist + weight
            if cost <= distances[neighbor][0]:
                if distances[node][1] == 'A':
                     tmp = distances[node][2] + transfer[node-1]
                else:
                    tmp = distances[node][2]
                distances[neighbor] = (cost,'B',tmp)
                heapq.heappush(q, (cost, neighbor))
    return distances
    
def solution(N, transfer, trainA, trainB, s, e):
    graphA = [[] for _ in range(N + 1)]
    graphB = [[] for _ in range(N + 1)]

    for u, v, w in trainA:
        graphA[u].append((v, w))
        graphA[v].append((u, w))

    for u, v, w in trainB:
        graphB[u].append((v, w))
        graphB[v].append((u, w))

    distancesA = dijkstra(graphA,graphB,transfer, s, N)
    distancesB = dijkstra(graphA,graphB,transfer, s, N)
    print(distancesA,distancesB)
    
    return distancesA[e][0] + distancesA[e][2]
N = 4
transfer = [1, 1, 2, 3]
trainA = [[1, 2, 1], [1, 3, 3], [2, 3, 3]]
trainB = [[1, 2, 3], [2, 3, 2], [3, 4, 1]]
s = 1
e = 4
result = solution(N, transfer, trainA, trainB, s, e)
print(result)