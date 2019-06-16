#Algoritmo con complessita' O(n^2 S(n)) dove S(n) e' il numero
#di matrici da stampare che dato l'intero n, stampa
#tutte le matrici ternarie n*n con la proprieta' che le righe e le colonne
#della matrice risultano ordinate in modo crescente.

n=2
set={1,2,3}

def mat(n):
    set={1,2,3}
    def es8(n,i=0,j=0):
        if i == n:
            for riga in range(n):
                print(sol[riga])
            print
        else:
            for x in set:
                if ( (i == 0 and j == 0) or
                     (j == 0 and x >= sol[i-1][j]) or
                     (i == 0 and x >= sol[i][j-1]) or
                     (x >= sol[i-1][j] and x >= sol[i-1][j-1] and x >= sol[i][j-1]) ):
                    sol[i][j] = x
                    if j < n-1:
                        es8(n,i,j+1)
                    else:
                        es8(n,i+1,0)
                    
    
    sol = [[0 for j in range(n)] for i in range(n)]
    es8(n)

mat(n)
