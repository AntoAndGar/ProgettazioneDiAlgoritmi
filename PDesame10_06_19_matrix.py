n=6

def PD(n) :
    z = len({'1','2','3','4'})
    T = [ [0 for _ in range(z)] for _ in range(n + 1)]
    for x in range(n+1):
        for y in range(z):
            if x == 0 :
                T [x][y] = 0
            elif x == 1:
                T [x][y] = 1
            elif x == 2 :
                if y == 0:
                    T [x][y] = 3
                if y == 1:
                    T [x][y] = 2
                if y == 2:
                    T [x][y] = 2
                if y == 3:
                    T [x][y] = 3
            else:
                if y == 0:
                    T [x][y] = T[x-1][y] + T[x-1][y+2] + T[x-1][y+3]
                if y == 1:
                    T [x][y] = T[x-1][y] + T[x-1][y+2]
                if y == 2:
                    T [x][y] = T[x-1][y] + T[x-1][y-2]
                if y == 3:
                    T [x][y] = T[x-1][y] + T[x-1][y-2] + T[x-1][y-3]
    return T [n]

print(PD(n))