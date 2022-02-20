import pprint

def resolver(matriz,a1,a2,a3):
    print("Matriz Inicial\n")
    print("\n".join([''.join(['{:4}'.format(item) for item in row]) for row in matriz]))
    
    pivAnt = 1
    print("\n")
    print("Proceso")
    for pivN in range(0, 3):
        print("\n")
        for r in range(0, 3):
            
            for c in range(0, 6):
                if c != pivN and r != pivN:
                    matriz[r][c] = int(round((matriz[pivN][pivN] * matriz[r][c] - matriz[r][pivN] * matriz[pivN][c]) / pivAnt))
            if r != pivN:
                matriz[r][pivN] = 0
            
        print("\n".join([''.join(['{:4}'.format(item) for item in row]) for row in matriz]))

        '''for mat in matriz:'''
        ''' print(matriz)'''
        '''print(str(matriz))'''
        pivAnt = matriz[pivN][pivN]
            
    print()
    print("Matriz final\n")
    print("\n".join([''.join(['{:4}'.format(item) for item in row]) for row in matriz]))
    det = matriz[0][0]
    x = a1 * matriz[0][3] / det + a2 * matriz[0][4] / det + a3 * matriz[0][5] / det
    y = a1 * matriz[1][3] / det + a2 * matriz[1][4] / det + a3 * matriz[1][5] / det
    z = a1 * matriz[2][3] / det + a2 * matriz[2][4] / det + a3 * matriz[2][5] / det
    
    print("\nValores de x,y,z:")
    print("X = " + str(x))
    print("Y = " + str(y))
    print("Z = " + str(z))
    return x,y,z