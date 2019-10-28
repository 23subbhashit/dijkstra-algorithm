graph = {'a':{'b':10,'c':3},'b':{'c':1,'d':2},'c':{'b':4,'d':8,'e':2},'d':{'e':7},'e':{'d':9}}
 
def dijkstra(graph,start,goal):
    s_dis= {}
    pre = {}
    notseen= graph
    infinity = 9999999
    path = []
    for node in notseen:
        s_dis[node] = infinity
    s_dis[start] = 0
 
    while notseen:
        mini = None
        for node in notseen:
            if mini is None:
                mini = node
            elif s_dis[node] < s_dis[mini]:
                mini = node
 
        for cNode, w in graph[mini].items():
            if w + s_dis[mini] < s_dis[cNode]:
                s_dis[cNode] = w + s_dis[mini]
                pre[cNode] = mini
        notseen.pop(mini)
 
    current= goal
    while current != start:
        try:
            path.insert(0,current)
            current = pre[current]
        except KeyError:
            break
    path.insert(0,start)
    if s_dis[goal] != infinity:
        print('Shortest distance is ' + str(s_dis[goal]))
        print('And the path is ' + str(path))
 
 
dijkstra(graph, 'a', 'b')

