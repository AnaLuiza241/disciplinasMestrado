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


# 2. Implemente o algoritmo QuickSort.
# 3. Implemete um árvore binária e seus algoritmos de caminhamento:
# (a) pre-order
# (b) pos-order
# (c) in-order

# 2 Conjunto 2 - Programa¸c˜ao Dinˆamica
# Cap´ıtulo 8 - Introduction to the Design and Analysis of Algorithms (3rd Edition) by Anany Levitin
# 1. Implemente os dois algoritmos baseados em programa¸c˜ao dinˆamica para o problem da mochila.
# (Se¸c˜ao 8.2)
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