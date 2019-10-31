graph = {"Bmsit1":{"Bmsit3":176,"Bmsit2":124},
	 "Bmsit2":{"Bmsit1":124,"Bmsit7":70},
         "Bmsit3":{"Bmsit4":58},
         "Bmsit4":{"Bmsit5":46,"Bmsit6":54},
	 "Bmsit5":{"Bmsit4":46},
         "Bmsit6":{"Bmsit7":176},
         "Bmsit7":{"Bmsit2":70,"Bmsit8":78},
         "Bmsit8":{"Bmsit9":130,"Bmsit7":78},
         "Bmsit9":{"Bmsit10":92,"Bmsit8":130},
         "Bmsit10":{"Bmsit7":74,"Bmsit8":117}}
 
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
        print(str(s_dis[goal]))
        print(str(path))
 
 
dijkstra(graph, "Bmsit1", "Bmsit10")

