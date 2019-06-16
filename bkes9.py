#Algoritmo con complessita' O(n^2 S(n)) dove S(n) e' il numero di
#matrici da stampare che dato l'intero n, stampa
#tutte le matrici binarie n*n con la proprieta' che nella matrice non
#compaiono mai due uni adiacenti in orizzontale, in verticale o in diagonale.

def mat(n):
    
    def es9(n, i = 0, j = 0):
        if i == n:
            for riga in range(n):
                print(M[riga])
            print
        else:
            M[i][j] = 0
            if j < n-1:
                es9(n, i, j + 1)
            else:
                es9(n, i + 1, 0)
            if  ((i-1 < 0 or M[i-1][j] == 0) and 
                (i-1 < 0 or j-1 < 0 or M[i-1][j-1] == 0) and 
                (i-1 < 0 or j+1 > n-1 or M[i-1][j+1] == 0) and
                (j-1 < 0 or M[i][j-1] == 0)):

                M[i][j] = 1
                if j < n-1:
                    es9(n, i, j + 1)
                else:
                    es9(n, i + 1, 0)

    M = [ [ 0 for j in range(n) ] for i in range(n) ]
    es9(n)

mat(3)
