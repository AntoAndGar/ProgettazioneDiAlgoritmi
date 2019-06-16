#Algoritmo con complessita' O(nS(n)) dove S(n) e' il numero di
#sequenza da stampare che presi i tre interi n, m e k,
#stampa tutte le sequenze di n interi positivi con interi di valore al piu'
#m e nelle quali nessun intero compare piu' di k volte.

n=3
m=2
k=2
set = set(range(1,m+1))

def bk6(n, k, tot=[0 for _ in range(m+1)], i = 0, sol=[]):
    if i == n:
        print(','.join(sol))
    else:
        for x in set:
            if tot[x] < k:
                sol.append(str(x))
                tot[x]=tot[x]+1
                bk6(n, k, tot, i + 1, sol)
                sol.pop()
                tot[x]=tot[x]-1

bk6(n, k)