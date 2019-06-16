#Algoritmo con complessita' O(n^2 S(n)) dove S(n) e' il numero
#di matrici da stampare che dato l'intero n, stampa
#tutte le matrici n * n e valori in {a, b, c} con la proprieta' che i simboli
#in ogni riga sono tutti uguali.

#ma questo e' backtracking? In teoria no perche' non usi funzioni di taglio 
#ma non generi proprio quelle soluzioni

n=2

def mat(n):

    set={'a','b','c'}

    def es7(n, i = 0, j = 0):
        if i == n:
            for riga in range(n):
                print(M[riga])
            print
        else:
            for x in set:
                for j in range(n):
                    M[i][j] = str(x)
                es7(n, i + 1, 0)

    M = [[0 for j in range(n)] for i in range(n)]
    es7(n)

mat(n)