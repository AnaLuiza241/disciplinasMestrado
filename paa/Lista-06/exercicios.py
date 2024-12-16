# 1 Conjunto 1 - Dividir e Conquistar

# 1. Implemente o algoritmo MergeSort.
## Complexidade: O(n*log n)
def merge_sort(a):
    n = len(a)
    if n > 1:
        b = a[:n//2]
        c = a[n//2:]
        b = merge_sort(b)
        c = merge_sort(c)
        a =  merge(b, c, a)
    return a

## Complexidade: O(n)
def merge (b, c, a):
    p = len(b)
    q = len(c)
    i = 0; j = 0; k = 0
    while (i < p) and (j < q):
        if b[i] <= c[j]:
            a[k] = b[i]
            i +=  1
        else:
            a[k] = c[j]
            j += 1
        k += 1
    if (i == p):
        a [k:] = c[j:]
    else:
        a[k:] = b[i:]
    return a



# 2 Conjunto 2 - Programação Dinâmica

# 1. Implemente os dois algoritmos baseados em programação dinâmica para o problema da mochila.
def knapsack(weights, values, n, W):
    F = [[0] * (W + 1) for _ in range (n + 1)]

    # Preenchendo a tabela de forma iterativa
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            if weights[i - 1] <= j: # Se o item cabe na mochila
                F[i][j] = max(F[i-1][j], values[i-1] + F[i -1][j - weights[i - 1]]) # Escolhe se inclui ou não o item na mochila
            else: # O item não cabe na mochila, então não inclui
                F[i][j] = F[i-1][j]
    
    return F[n][W]


def mf_knapsack(weights, values, n, W):
    # Tabela de memória
    F = [[-1] * (W +1) for _ in range(n + 1)]

    def helper(i, j):
        if F[i][j] < 0: # Se ainda não calculou
            if i == 0 or j == 0: # Caso base
                F[i][j] = 0
            elif weights[i -1] > j: # O peso do item é maior que a capacidade, então ignora o item
                F[i][j] = helper(i - 1, j)
            else: # Escolhe entre incluir ou não incluir
                F[i][j] = max(helper(i - 1, j), # Ignora o item
                            values[i - 1] + helper(i - 1, j - weights[i - 1])  )
        return F[i][j]
    
    return helper(n, W)



# 3 Conjunto 3 - Algoritmos Gulosos
# Chapter 9 - Introduction to the Design and Analysis of Algorithms (3rd Edition) by Anany Levitin
# 1. Implemente o algoritmo de Prim.
# 2. Implemente o algorimo de Kruskall.
# 3. Implemente o algoritmo de Dijkstra.
# 1
# 4 Conjunto 4 - Backtracking
# Se¸c˜ao 12.1 - Introduction to the Design and Analysis of Algorithms (3rd Edition) by Anany Levitin
# 1. Implemente um algoritmo baseado em backtracking para o problema das n-rainhas.
# 2. Implemente um algoritmo baseado em backtracking para o problem ( subset-sum).
# 5 Conjunto 5 - Branch and Bound
# Se¸c˜ao 12.2 - Introduction to the Design and Analysis of Algorithms (3rd Edition) by Anany Levitin
# 1. Implemente um algoritmo baseado em branch and bound para o problema da mochila.
# 2. Implemente um algoritmo baseado em branch and bound para o problema do caixeiro viajante.