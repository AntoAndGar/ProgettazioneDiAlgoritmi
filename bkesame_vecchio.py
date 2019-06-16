#Algoritmo che, dato l'intero n, stampa tutte le sequenze ternarie lunghe n 
#in cui la cifra 2 puo' avere come cifra adiacente solo lo zero

n=3
set = set([x for x in range(3)])

def bk(n, i = 0, sol = []):
    if i==n:
        print(''.join(sol))
    else:
        for x in set:
            #if x not in sol or (i > 0 and x == 2 and sol[i-1] == 0):
            if x != 2 or (i > 0 and (int(sol[i-1]) == 0)) or (n-i > 0 and x == 2) :  
                sol.append(str(x))
                bk(n, i + 1, sol)
                sol.pop()

bk(n)

