import random
#M = [[1,0,1,1,1],
#     [1,1,1,1,1],
#     [1,1,1,0,1],
#     [1,1,1,1,1],
#     [1,1,0,1,1]]


#M=[[1, 1, 1, 0, 1, 1, 0],
#[1, 0, 1, 1, 1, 0, 1],
#[1, 1, 0, 1, 1, 1, 0],
#[1, 1, 1, 1, 1, 1, 0],
#[0, 1, 1, 1, 1, 0, 0],
#[0, 0, 1, 1, 1, 1, 1],
#[1, 1, 0, 1, 1, 1, 1]]
#

def create_rand_matrix(n):
    M = [[-1 for _ in range(n)] for _ in range(n)]
    for i in range (len(M)):
        for j in range (len(M)):
            if (random.randint(1,10) > 9): #il valore serve per "dosare" la quantita' di uni presente dnella tabella random creata
                M[i][j] = 0
            else:
                M[i][j] = 1
            #M[i][j] = random.randint(0, 1) #questa e' per creare una matrice completamente random 
    return M

M = create_rand_matrix(10)
for i in range(len(M)):
    print(M[i])

print('\n')

#T = [[] for _ in range(len(M))]

def PDes4(M):
    T = [[-1 for _ in range(len(M))] for _ in range(len(M))]
    max_submatrix = -1
    for i in range (len(M)):
        for j in range (len(M)):
            if i == 0:
                if M[i][j] == 1:
                    T[i][j] = 1
                    max_submatrix = 1
                else:
                    T[i][j] = 0
                    max_submatrix = 0
            if j == 0:
                if M[i][j] == 1:
                    T[i][j] = 1
                else:
                    T[i][j] = 0
            if j != 0 and i != 0:
                if M[i][j] == 0:
                    T[i][j] = 0
                elif T[i-1][j-1] == T[i-1][j] == T[i][j-1]:
                    T[i][j] = T[i-1][j] + 1
                    max_submatrix = max(max_submatrix, T[i][j])
                elif (( T[i-1][j-1] == 0 or T[i-1][j] == 0 or T[i][j-1] == 0 ) and ( M[i][j] == 1 )):
                    T[i][j] = 1
                elif ( T[i-1][ j-1] != 0 and T[i-1][j] != 0 and T[i][j-1] != 0 ):
                    T[i][j] = min(T[i-1][j-1], T[i-1][j], T[i][j-1]) + 1
    for i in range (len(M)):
        print(T[i])
    print("Result: "+str(max_submatrix))

PDes4(M)
    