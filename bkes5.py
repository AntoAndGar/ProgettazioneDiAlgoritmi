#Algoritmo con complessita' O(n^2 S(n)) dove S(n) e' il numero
#di permutazioni da stampare che dato l'intero pari n, stampa
#tutte le permutazioni dei primi n interi in cui nell'ordinamento non
#appaiono mai due pari consecutivi ne' due dispari consecutivi.

n = 4
list = [x for x in range(1, n + 1)]

def bk5(n, i = 0, sol = []):
    if i == n:
        print(''.join(sol))
    else:
        for x in list:
            if (str(x) not in sol and (i==0 or x%2 != int(sol[i-1])%2)):
                sol.append(str(x))
                bk5(n, i + 1, sol)
                sol.pop()

bk5(n)