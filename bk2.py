def bk2(n, k, i = 0, tot1 = 0, sol = []) :
    if i == n :
        print(''.join(sol))
    else:
        sol.append('0')
        bk2(n, k, i + 1, tot1, sol)
        sol.pop()
        if tot1 < k:
            sol.append('1')
            bk2(n, k, i + 1, tot1 + 1, sol)
            sol.pop()

bk2(4,1)