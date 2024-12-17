from exercicios import *


def teste_MergeSort():
    v = [([], []), ([1], [1]), 
         ([8, 1, 5, 7, 3, 2, 6, 4, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]), 
         ([-1, 7, 9, 43, -27, 1, 9, 12], [-27, -1, 1, 7, 9, 9, 12, 43])]
    i = 0
    print('Testes Merge Sort:')
    for (e, s) in v:
        entrada = e.copy()
        resultado = merge_sort(entrada)
        i += 1
        assert resultado == s, f"Teste {i} falhou! Estrada: {e} Esperado: {s}, Obtido: {resultado}"
        print(f'Teste {i} passou! Entrada: {e}  Resultado: {s}')
    print()
    
def test_problema_mochila():
    v = [(2, 12, [10, 5], [100, 200], 200),
         (4, 5, [2, 3, 4, 5], [3, 4, 5, 6], 7),
         (10, 15, [1, 2, 3, 8, 7, 4, 5, 6, 9, 5], [20, 30, 40, 100, 90, 50, 60, 70, 80, 30], 200)
        ]
    print('Testes Problema da Mochila:')
    i = 0
    for p in v:
        n, C, pesoI, lucroI, lucro_ideal = p
        print('Problema Mochila Programação Dinâmica versão 1')
        l = knapsack(pesoI, lucroI, n, C)
        i += 1
        assert l == lucro_ideal, f"Teste {i} falhou! Lucro Esperado: {lucro_ideal}, Obtido: {l}"
        print(f'Teste {i} passou! Lucro: {l}')

        print('Problema Mochila Programação Dinâmica versão 2')
        l = mf_knapsack(pesoI, lucroI, n, C)
        i += 1
        assert l == lucro_ideal, f"Teste {i} falhou! Lucro Esperado: {lucro_ideal}, Obtido: {l}"
        print(f'Teste {i} passou! Lucro: {l}')
        print()
    print()

def teste_kruskal():
    v = [([[0,1,4,1,0,16],
          [1,0,0,9,0,8],
          [4,0,0,0,3,24],
          [1,9,0,0,0,7],
          [0,0,3,0,0,2],
          [16,8,24,7,2,0]], 11),
          ([[0]], 0), 
          ([[0,1,0,0],
            [0,0,5,2],
            [4,0,0,0],
            [6,0,3,0]], 6)
    ]
    i = 0
    print('Testes Kruskal:')
    for g,c in v:
        arvore, custo = kruskall(g)
        assert custo == c, f"Teste {i} falhou! Árvore obtida: {arvore} Esperado: {c}, Obtido: {custo}"
        print(f'Teste {i} passou! Árvore obtida: {arvore}  Resultado: {c}')
    print()

def teste_subset_sum():

    v = [
        ([3, 5, 6, 7], 15, True),  # Existe um subconjunto
        ([1, 2, 3, 7], 52, False), # Não existe um subconjunto
        ([1, 2, 3, 7], 10, True),  # Existe um subconjunto
        ([2, 4, 6], 5, False),     # Não existe um subconjunto
        ([], 0, True),             # Subconjunto vazio é uma solução válida
    ]

    print('Testes Subset Sum:')
    for i, (lista, alvo, esperado) in enumerate(v, 1):
        resultado = subset_sum(lista, alvo)
        if esperado:
            assert sum(resultado) == alvo, (
                f"Teste {i} falhou! Entrada: {lista}, Alvo: {alvo}, "
                f"Esperado: Solução válida, Obtido: {resultado}"
            )
            print(f'Teste {i} passou! Entrada: {lista}, Alvo: {alvo}, Resultado: {resultado}')
        else:
            assert resultado == [], (
                f"Teste {i} falhou! Entrada: {lista}, Alvo: {alvo}, "
                f"Esperado: Sem solução, Obtido: {resultado}"
            )
            print(f'Teste {i} passou! Entrada: {lista}, Alvo: {alvo}, Resultado: Sem solução')
    print()


def test_problema_mochila_branch_bound():
    v = [(2, 12, [10, 5], [100, 200], 200),
         (4, 5, [2, 3, 4, 5], [3, 4, 5, 6], 7),
         (10, 15, [1, 2, 3, 8, 7, 4, 5, 6, 9, 5], [20, 30, 40, 100, 90, 50, 60, 70, 80, 30], 200)
        ]
    print('Testes Problema da Mochila Branch and Bound:')
    i = 0
    for p in v:
        n, C, pesoI, lucroI, lucro_ideal = p
        l = mochila_branch_and_bound(lucroI, pesoI, C)
        i += 1
        assert l == lucro_ideal, f"Teste {i} falhou! Lucro Esperado: {lucro_ideal}, Obtido: {l}"
        print(f'Teste {i} passou! Lucro: {l}')
    print()