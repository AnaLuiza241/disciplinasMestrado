# Exercício 1: Implementar o Selection Sort

def selection_sort(arr):
    n = len(arr)
    ordenado = [0]*n

    for i in range(n):
        m = len(arr)
        menor = arr[0]
        i_menor = 0
        for j in range(m):
            if arr[j] < menor:
                menor = arr[j]
                i_menor = j
        ordenado[i] = menor
        arr.pop(i_menor)

    return ordenado

# Exercício 2: Implementar o Sequencial Search2 do livro

def sequential_search2(arr, k):
    n = len(arr)
    arr.append(k)
    i = 0
    while arr[i] != k:
        i += 1
    
    if i < n:
        return i
    return -1

# Exercício 3: Implementar Busca em Largura (BFS)

def bfs(listaAdj, s = 0):
    visitados = []
    L = [s]
    n = len(listaAdj)

    while L:
        elem = L.pop(0)
        if not (elem in visitados):
            visitados.append(elem)
            lista = listaAdj[elem]
            for l in lista:
                L.append(l)

    return visitados

def bfsv2(listaAdj, d, s = 0):
    visitados = []
    L = [s]

    while L:
        elem = L.pop(0)
        if elem == d:
            visitados.append(elem)
            return visitados
        if not (elem in visitados):
            visitados.append(elem)
            lista = listaAdj[elem]
            for l in lista:
                L.append(l)

    return visitados

# Exercício 4: Implementar Busca em Profundidade (DFS)

def dfs(listaAdj, s = 0):
    visitados = []
    L = [s]

    while L:
        elem = L.pop()
        if not (elem in visitados):
            visitados.append(elem)
            lista = listaAdj[elem]
            while lista:
                l = lista.pop()
                L.append(l)
        
    return visitados

def dfsv2(listaAdj, d, s = 0):
    visitados = []
    L = [s]

    while L:
        elem = L.pop()
        if elem == d:
            visitados.append(elem)
            return visitados
        if not (elem in visitados):
            visitados.append(elem)
            lista = listaAdj[elem]
            while lista:
                l = lista.pop()
                L.append(l)
        
    return visitados
# Exercício 5: Implementar Problema do Caixeiro Viajante

def caixeiroViajante(cidade_inicial, domain, matriz_de_custo):
    s_ideal = []
    c_ideal = float("inf")
    L = [[cidade_inicial]]
    n = len(domain)

    while L:
        s = L.pop(0)
        if len(s) == n:
            custo = 0
            for i in range(0,n-1):
                custo += matriz_de_custo[s[i]][s[i+1]]
            custo += matriz_de_custo[s[-1]][cidade_inicial]
            if custo < c_ideal:
                c_ideal = custo
                s_ideal = s
        else:
            for e in domain:
                if not (e in s):
                    L.append(s+[e])
    return s_ideal, c_ideal

# Exercício 6: Implementar Problema da mochila com busca exaustiva

def problemaMochila(n,C, pesoI, lucroI, domain=[0,1]):
    s_ideal = [0]*n
    lucroIdeal = 0
    L = []
    
    for e in domain:
        L.append([e])
    
    while L:
        s = L.pop()
        if len(s) == n:
            custo = 0
            lucro = 0
            i = 0
            for item in s:
                custo += pesoI[i]*item
                lucro += lucroI[i]*item
                i += 1
            if custo <= C:
                if lucro > lucroIdeal:
                    s_ideal = s
                    lucroIdeal = lucro
        else:
            for e in domain:
                L.append(s+[e])
    
    return s_ideal, lucroIdeal

# Exercício 7: Encontrar o menor caminho de uma grade de tamnho nxn

def labirinto(grid):
    n = len(grid)
    qtd_c = 0
    L = []
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                L.append([(i,j)])
                continue
    
    while L:
        s = L.pop()
        i, j = s[-1]
        # Indo pra cima
        if i > 0:
            if grid[i-1][j] == 2:
                qtd_c += 1
            if (grid[i-1][j] == 3) and ((i-1, j) not in s):
                L.append(s+[(i-1,j)])
        # Indo para baixo
        if i < n-1:
            if grid[i+1][j] == 2:
                qtd_c += 1
            if (grid[i+1][j] == 3) and ((i+1, j) not in s):
                L.append(s+[(i+1, j)])
        # Indo para a esquerda
        if j > 0:
            if (grid[i][j-1] == 2) and ((i, j-1) not in s):
                qtd_c +=1
            if grid[i][j-1] == 3:
                L.append(s+[(i, j-1)])
        # Indo para a direita
        if j < n-1:
            if grid[i][j+1] == 2:
                qtd_c += 1
            if (grid[i][j+1] == 3) and ((i, j+1) not in s):
                L.append(s+[(i,j+1)])

    return qtd_c

if __name__ == '__main__':
    print('Testes dos exercícios:\n')

    print('Exercício 1 _ Selection Sort:')
    print(selection_sort([1,2,3,4]))
    print(selection_sort([4,3,2,1]))
    print(selection_sort([2,74,81,6,35,47,2,4,7,8,10,15]))
    print()

    print('Exercício 2 _ Sequeantial Search:')
    print(sequential_search2([0,1,2,3,4,5], 6))
    print(sequential_search2([0,1,2,3,4,5], 0))
    print(sequential_search2([0,1,2,3,4,5], 5))
    print(sequential_search2([2,74,46,14,81,7], 14))
    print()

    print('Exercício 3 _ Busca em Largura:')
    print(bfs([[1,2,3],[0],[0,4],[0],[2]]))
    print(bfs([[],[2,3,6],[1,10],[1,5,8,9,10,12],[10,12],[3,6,8],[1,5,11],[8,11],[3,5,7,12],[3,10],[3,4,9],[6,7],[3,4,8]], s=1))
    print(f'Com destino 4: {bfsv2([[1,2,3],[0],[0,4],[0],[2]], d=4)}')
    print(f'Com destino 11: {bfsv2([[],[2,3,6],[1,10],[1,5,8,9,10,12],[10,12],[3,6,8],[1,5,11],[8,11],[3,5,7,12],[3,10],[3,4,9],[6,7],[3,4,8]], d=11, s=1)}')
    print()

    print('Exercício 4 _ Busca em Profundidade:')
    print(dfs([[1,2,3],[0],[0,4],[0],[2]]))
    print(dfs([[],[2,3,6],[1,10],[1,5,8,9,10,12],[10,12],[3,6,8],[1,5,11],[8,11],[3,5,7,12],[3,10],[3,4,9],[6,7],[3,4,8]], s=1))
    print(f'Com destino 4: {dfsv2([[1,2,3],[0],[0,4],[0],[2]], d=4)}')
    print(f'Com destino 11: {dfsv2([[],[2,3,6],[1,10],[1,5,8,9,10,12],[10,12],[3,6,8],[1,5,11],[8,11],[3,5,7,12],[3,10],[3,4,9],[6,7],[3,4,8]], d=11, s=1)}')
    print()    

    print('Exercício 5 _ Caixeiro Viajante:')
    s, c = caixeiroViajante(0, [0,1,2,3], [[float("inf"), 1, 1, -1], [1, float("inf"), 3, 2], [1, 3, float("inf"), 3], [-1, 2, 3, float("inf")]])
    print(f's:{s}   c:{c}')
    print()

    print('Exercício 6 _ Problema da Mochila:')
    s, l = problemaMochila(2, 12, [10, 5], [100, 200])
    print(f's: {s}  lucro:{l}')
    s, l = problemaMochila(4, 5, [2, 3, 4, 5], [3, 4, 5, 6])
    print(f's: {s}  lucro:{l}')
    s, l = problemaMochila(10, 15, [1, 2, 3, 8, 7, 4, 5, 6, 9, 5], [20, 30, 40, 100, 90, 50, 60, 70, 80, 30])
    print(f's: {s}  lucro:{l}')
    print()

    print('Exercício 7 _ Labirinto:')
    m0 = [[3, 0, 3, 0, 0], 
          [3, 0, 0, 0, 3],
          [3, 3, 3, 3, 3],
          [0, 2, 3, 0, 0],
          [3, 0, 0, 1, 3]]
    
    m1 =  [[1, 3],
           [3, 2]]
    
    m2 = [[0, 3, 3, 0, 0, 0, 0, 0, 0, 0],
          [0, 3, 2, 3, 3, 3, 0, 0, 0, 0],
          [0, 3, 0, 3, 0, 3, 0, 0, 0, 0],
          [0, 3, 0, 3, 0, 3, 0, 0, 0, 0],
          [0, 3, 0, 3, 0, 3, 0, 0, 0, 0],
          [0, 3, 0, 3, 3, 3, 3, 0, 0, 0],
          [0, 3, 0, 0, 0, 3, 1, 0, 0, 0],
          [0, 3, 0, 0, 0, 0, 3, 0, 0, 0],
          [0, 3, 0, 0, 0, 0, 3, 0, 0, 0],
          [0, 3, 3, 3, 3, 3, 3, 0, 0, 0]]
    
    m3 = [[0, 3, 3, 3, 1],
          [0, 3, 0, 0, 3],
          [0, 2, 0, 0, 3],
          [0, 3, 0, 0, 3],
          [0, 3, 3, 3, 3]]

    print(labirinto(m0))
    print(labirinto(m1))
    print(labirinto(m2))
    print(labirinto(m3))
    print()