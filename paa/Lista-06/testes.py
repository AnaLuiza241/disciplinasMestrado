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
    