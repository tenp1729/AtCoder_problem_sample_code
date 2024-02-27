from heapq import heappop, heappush


"""
ダイクストラ法の部分。
edgesである頂点からどこの頂点へつながっているか、かかる時間、列車情報を受け取る。
num_nodeは最速時刻と頂点を保持する。
startがダイクストラ法の始点(今回はn-1確定だが流用できるようにdijkstraの関数をつくってある)
heapqを使うとNlogNで計算できる。
この形になるようにdiaを定義している。
"""
def dijkstra(edges, num_node, start):
    node = [10 ** 18 for _ in range(num_node)]
    node[start] = -10 ** 20
    n_node = [[-10 ** 20, start]]
    used = [False for _ in range(num_node)]
    while n_node:
        d, min_node = heappop(n_node)
        used[min_node] = True
        for goal, cost, dl in edges[min_node]:
            if used[goal]:
                continue
            if dl[0] >= d and (x := (min(dl[2] - 1, ((d - dl[0]) // dl[1])) * dl[1] + dl[0])) + cost < node[goal]:
                node[goal] = x + cost
                heappush(n_node, [node[goal], goal])
    return node


n, m = map(int, input().split())
train = [list(map(int, input().split())) for _ in range(m)]
dia = [[] for i in range(n)]
for i in range(m):
    dia[train[i][5] - 1].append([train[i][4] - 1, train[i][3], [-train[i][0] - train[i][3], -train[i][1], train[i][2]]])
ans = dijkstra(dia, n, n - 1)
for i in range(n - 1):
    if ans[i] < 0:
        print(-ans[i])
    else:
        print("Unreachable")
