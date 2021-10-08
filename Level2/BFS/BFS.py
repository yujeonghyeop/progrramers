from collections import deque #deque를 쓰기위한 모듈 import

def bfs(graph,root):
    visit=set() #효율성을 위해 visit을 list가 아닌 set으로 정의한다. 중복이 자동으로 삭제되기 때문에 훨씬 효율적
    queue=deque([root]) #queue를 deque로 정의하고 root_node를 적는다.
    visit.add(root) #visit에도 root_node를 추가한다.
    while queue:
        n = queue.popleft() #queue에서 pop하듯이 deque를 popleft하여 n에 저장한다.
        print(n, end='->')    #visit이 set이기 때문에 visit을 출력하면 안되고 deque에서 pop된 친구들을 출력해야한다.
        for neighbour in graph[n]: 
            if neighbour not in visit: #만약 graph[n]의 인덱스가 visit에 없다면 
                visit.add(neighbour)    #visit에 추가를 해준다.(더이상 가면 안되기 때문에) 여기서 중복이 들어오게 되면 set이기 때문에 자동으로 삭제된다.
                queue.append(neighbour) #다음 그래프 순회를 하기 위해 deque에 추가해준다. 

graph_list = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}
print(graph_list)
root_node = 'A'
bfs(graph_list,root_node)