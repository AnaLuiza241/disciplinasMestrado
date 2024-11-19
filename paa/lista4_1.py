import copy
import math
import matplotlib.pyplot as plt

# 1. Implementar o algoritmo BubbleSort
def bubblesort (arr):
    n = len(arr)
    a = copy.copy(arr)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            #print(a, end=' ')
            if a[j + 1] < a[j]:
                #print(f'({j+1} troca com {j})')
                aux = a[j]
                a[j] = a[j+1]
                a[j+1] = aux
            #else:
                #print(f'({j+1} não troca com {j})')
                #continue
    return a

# 2. Implementar o Brute Force String Matching
def bfStringMatch (t, p):
    n = len(t)
    m = len(p)
    for i in range(n-m+1):
        j = 0
        while (j < m) and (p[j] == t[i +j]):
            j += 1
        if j == m:
            return i

    return -1 

# 3. Implementar o Brute Force Closest Pair
def bfClosestPair(P):
    d = float('inf')
    n = len(P)
    pares = []
    for i in range(n-1):
        for j in range(i+1, n):
            xi, yi, xj, yj = P[i][0], P[i][1], P[j][0], P[j][1]
            distancia = math.sqrt((xi - xj)**2 + (yi - yj)**2)
            if distancia < d:
                d = distancia
                pares = [(xi, yi), (xj, yj)]
    return d, pares

# 4. Implementar o Brute Force Convex Hull
def bfConvexHull(P):
    n = len(P)
    hull = []
    for i in range(n-1):
        for j in range(i + 1, n):
            x1, y1 = P[i][0], P[i][1]
            x2, y2 = P[j][0], P[j][1]
            a = y2 - y1
            b = x1 - x2
            c = x1*y2 - y1*x2
            pos = True
            neg = True
            for k in range(n):
                if (k != i) and (k != j):
                    xk, yk = P[k][0], P[k][1]
                    valor = a*xk + b*yk - c
                    if valor > 0:
                        neg = False
                    elif valor < 0:
                        pos = False
            if pos or neg:
                hull.append([P[i], P[j]])
    return hull  

def plot_convex_hull(P, hull):
    """
    Plota os pontos e conecta os pares de pontos do convex hull com linhas.

    Parâmetros:
    - P: lista de tuplas, representando os pontos (x, y).
    - hull: lista de pares de tuplas, onde cada par é um segmento [(x1, y1), (x2, y2)].
    """
    # Desempacotando os pontos
    x_points, y_points = zip(*P)
    
    # Plotando os pontos
    plt.scatter(x_points, y_points, label="Pontos", color="blue", zorder=2)

    # Para cada segmento no hull, desenha uma linha conectando os pontos
    for (x1, y1), (x2, y2) in hull:
        plt.plot([x1, x2], [y1, y2], color="red", zorder=1)

    # Adicionando informações ao gráfico
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Convex Hull")
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
    plt.legend(["Hull", "Pontos"])
    plt.grid(True)
    plt.axis('equal')  # Para manter as proporções corretas no gráfico
    plt.show()



if __name__ == "__main__":
    print('Teste das Implementações \n')
    
    print('Exercício 1: Bubble Sort:')
    a = bubblesort([15, 1, 4, 6, 8, 7, 13, 24, 58, -6])
    print(a)
    print()

    print('Exercício 2: Brute Force String Matching:')
    frase = "O rápido desenvolvimento da tecnologia transformou a maneira como vivemos e trabalhamos."
    substrings = ["rápido", "tecnologia", "transformou", "maneira", "vivemos", "trabalhamos", "desenvolvimento", "forma", "O rápido", "trabalhos", "o desenvol", "logia", "O"," ", "."]
    print(frase)
    for s in substrings:
        print(f'subString:{s}   Posição inicial:{bfStringMatch(frase,s)}')
    print()

    print('Exercício 3: Brute Force Closest Pair:')
    P = [(1, 1), (-5, 1), (15, 7), (0, 0), (8, -2), (-1, 0)] 
    print(bfClosestPair(P))
    print()

    print('Exercício 4: Brute Force Convex Hull:')
    P = [(5.15, -3.07), (-3.2, 1.8), (-5.7, -2.75), (-0.52, -1.28), (1.1, 5), (-0.42, -5.06), (-1.27, -0.93), (5.9, - .23)]
    hull = bfConvexHull(P) 
    print(hull)
    plot_convex_hull(P, hull)

