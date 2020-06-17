"""
2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
"""
g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]

def deikstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    way = [[], ]

    cost[start] = 0
    min_cost = 0
    # while min_cost < float('inf'):
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    # print(f'parent: {parent}')
                    # print(f'Node: {i}')

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    return cost, parent


start = int(input('Введите начальную вершину:\n'))
dejk, par = deikstra(g, start)
print(dejk)
def find_path(start, end):
    path = list()
    while start != par[end]:
        if par[end] == -1:
            break
        path.append(par[end])
        end = par[end]
    path.append(start)
    return f'path {path}'

a = find_path(0, 2)

for itm, vertex in enumerate(dejk):
    a = find_path(start, itm)
    if vertex != float('inf'):
        print(f'Path for {itm} is: {a}. And cost is: {vertex}')
    else: print(f'Path for {itm} is: None')