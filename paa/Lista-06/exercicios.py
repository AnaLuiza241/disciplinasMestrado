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

# 2. Implemente o algorimo de Kruskall.

def ordena_arestas(G):
    a = []
    n_vertices = len(G)

    for i in range(n_vertices):
        for j in range(n_vertices):
            if G[i][j] > 0:
                a.append((G[i][j], i, j))
    
    a.sort(key=lambda x: x[0])
    return a

def kruskall (G):
    
    n_vertices = len(G)
    edges = ordena_arestas(G)
    Et = []
    peso_total = 0
    conjuntos = {v: {v} for v in range(n_vertices)}
    ecounter = 0
    k = 0

    while (ecounter < n_vertices - 1):
        peso, u, v = edges[k]
        k += 1
        if conjuntos[u] is not conjuntos[v]:
            Et.append((peso, u, v))
            peso_total += peso
            ecounter += 1
            conjunto_u = conjuntos[u]
            conjunto_v = conjuntos[v]
            novo_conjunto = conjunto_u.union(conjunto_v)
            for w in novo_conjunto:
                conjuntos[w] = novo_conjunto
            
    
    return Et, peso_total
        
# 4 Conjunto 4 - Backtracking

# 2. Implemente um algoritmo baseado em backtracking para o problem ( subset-sum).

def subset_sum(A, d):
    L = [([], 0)]
    n = len(A)

    while L:
        s, index = L.pop() 
        
        soma = sum(s)

        if soma == d:
            return s

        if soma < d and index < n:
            L.append((s + [A[index]], index + 1))
            L.append((s, index + 1))

    return []


# 5 Conjunto 5 - Branch and Bound

# 1. Implemente um algoritmo baseado em branch and bound para o problema da mochila.

def calcula_limite(node, W, itens, n):
    """Calcula o limite superior (bound) de um nó."""
    if node["peso"] > W:
        return 0  # Se o peso excede a capacidade, o limite é 0

    valor = node["valor"]
    peso = node["peso"]
    i = node["nivel"] + 1

    # Adiciona itens inteiros enquanto houver capacidade
    while i < n and peso + itens[i][1] <= W:
        peso += itens[i][1]
        valor += itens[i][0]
        i += 1

    # Adiciona fração do próximo item, se houver capacidade
    if i < n:
        valor += (W - peso) * (itens[i][0] / itens[i][1])

    return valor


def mochila_branch_and_bound(valores, pesos, W):
    """Resolve o problema da mochila usando Branch and Bound."""
    # Ordena itens por valor/peso em ordem decrescente
    n = len(valores)
    itens = sorted(zip(valores, pesos), key=lambda x: x[0] / x[1], reverse=True)

    # Inicializa a solução
    melhor_valor = 0
    fila = []

    # Adiciona o nó raiz
    raiz = {"nivel": -1, "valor": 0, "peso": 0, "limite": 0}
    raiz["limite"] = calcula_limite(raiz, W, itens, n)
    fila.append(raiz)

    # Exploração da árvore de estado
    while fila:
        node = fila.pop(0)  # Retira o primeiro nó da fila

        # Se o nó for promissor
        if node["limite"] > melhor_valor and node["nivel"] < n - 1:
            # Próximo item
            nivel = node["nivel"] + 1
            peso_atual = node["peso"]
            valor_atual = node["valor"]

            # Nó incluindo o próximo item
            if peso_atual + itens[nivel][1] <= W:
                incluir = {
                    "nivel": nivel,
                    "peso": peso_atual + itens[nivel][1],
                    "valor": valor_atual + itens[nivel][0],
                    "limite": 0,
                }
                incluir["limite"] = calcula_limite(incluir, W, itens, n)

                if incluir["valor"] > melhor_valor:
                    melhor_valor = incluir["valor"]

                fila.append(incluir)

            # Nó excluindo o próximo item
            excluir = {
                "nivel": nivel,
                "peso": peso_atual,
                "valor": valor_atual,
                "limite": 0,
            }
            excluir["limite"] = calcula_limite(excluir, W, itens, n)

            fila.append(excluir)

    return melhor_valor
