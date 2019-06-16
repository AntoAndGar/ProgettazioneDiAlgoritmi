def str(n, i = 0, sol = []):
    if i == n :
        print(''.join(sol))
        return
    for c in {'0','1','2'}:
        sol.append(c)
        str( n, i+1, sol)
        sol.pop()

str(4)