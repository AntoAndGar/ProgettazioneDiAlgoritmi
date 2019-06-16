#Algoritmo con complessita' O(nS(n)) dove S(n) e' il numero
#di matrici da stampare che dato l'intero n, stampa
#tutte le sequenze lunghe n formate da interi nell'insieme {1, 2, 3, 4}
#con la proprieta' che nella sequenza numeri adiacenti distano almeno 2.

n=3
set={1,2,3,4}

def es4(n,i = 0,sol=[]):
    if i == n:
        print(''.join(sol))
    else:
        for x in set:
            if i == 0 or (abs(int(sol[i-1])-x) > 1):
                sol.append(str(x))
                es4(n,i+1,sol)
                sol.pop()

es4(n)