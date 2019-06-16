#complessita' dell' algoritmo O(n*S(n))

def str(n, i = 0, sol = []):
    tot=0
    if i == n :
        return 1
    for c in {'0','1','2'}:
        if (i == 0) or (c == '1') or (c == '0' and sol[i-1] != '2') or (c == '2' and sol[i-1] != '0'):
            sol.append(c)
            tot += str( n, i+1, sol)
            sol.pop()
    return tot

print(str(5))

