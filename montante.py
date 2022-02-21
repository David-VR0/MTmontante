import pprint

def resolver(matriz,a1,a2,a3):
    print("Matriz Inicial\n")
    print("\n".join([''.join(['{:6}'.format(item) for item in row]) for row in matriz]))
    
    pivAnt = 1
    print("\n")
    print("Proceso")
    for pivAct in range(0, 3):
        print("\n")
        for f in range(0, 3):
            
            for c in range(0, 6):
                if c != pivAct and f != pivAct:
                    matriz[f][c] = float(round((matriz[pivAct][pivAct] * matriz[f][c] - matriz[f][pivAct] * matriz[pivAct][c]) / pivAnt))
            if f != pivAct:
                matriz[f][pivAct] = 0
            
        print("\n".join([''.join(['{:6}'.format(item) for item in row]) for row in matriz]))

        '''for mat in matriz:'''
        ''' print(matriz)'''
        '''print(str(matriz))'''
        pivAnt = matriz[pivAct][pivAct]
            
    print()
    print("Matriz final\n")
    print("\n".join([''.join(['{:6}'.format(item) for item in row]) for row in matriz]))
    det = matriz[0][0]
    print("\n Determinante:",det)
    x = round(a1 * matriz[0][3] / det + a2 * matriz[0][4] / det + a3 * matriz[0][5] / det,6)
    y = round(a1 * matriz[1][3] / det + a2 * matriz[1][4] / det + a3 * matriz[1][5] / det,6)
    z = round(a1 * matriz[2][3] / det + a2 * matriz[2][4] / det + a3 * matriz[2][5] / det,6)

    inversa = [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(0, 3):
        for j in range(0, 3):
            inversa[i][j]=str(matriz[i][j+3])+"/"+str(det)+"  "

    print("\nInversa \n")
    print("\n".join([''.join(['{:10}'.format(item) for item in row]) for row in inversa]))

    print("\nValores de x1,x2,x3:")
    print("X1 = " + str(x))
    print("X2 = " + str(y))
    print("X3 = " + str(z))
    return x,y,z