def dfs(graph, start_node,visit=list()):    #visit을 재귀로 계속 받아주기 위해 함수 인자에 list로 정의한 후 설정해준다.
    visit.append(start_node)    #start_node의 인자로 들어온 문자를 visit리스트에 추가해준다.
    print(start_node, end='->') #들어온 node를 출력해준다.
    for node in graph[start_node]:  
        if node not in visit:   #만약 grpah[start_node]의 인덱스가 visit리스트에 없다면 거쳐간 것이 아니기 때문에 
            dfs(graph,node,visit)   #재귀로 visit 리스트까지 다시 dfs함수로 보내준다. visit함수에 있다면 거쳐간 것이므로 넘어가게 된다. 
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
dfs(graph_list,'A')