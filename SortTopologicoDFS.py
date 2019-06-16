
def SortT(x):

    G={
    0:[5],
    1:[2,7],
    2:[5,6],
    3:[0,2],
    4:[0,3],
    5:[],
    6:[],
    7:[6,2]
    }

    def DFS(x):
        for y in G[x]:
            if V[y] == 0:
                V[y] = 1
                DFS(y)
        ST.append(x)

    V=[0 for _ in G]
    ST=[]
    for u in G:
        if V[u] == 0:
            V[u] = 1
            DFS(u)
    ST.reverse()
    return ST

print(SortT(1))