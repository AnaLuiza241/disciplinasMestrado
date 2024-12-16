from exercicios import *
from lista4 import *

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