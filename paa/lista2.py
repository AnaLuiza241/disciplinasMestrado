# # Lista de Exercícios 2
 
# ## Arrays

# 1. Missing in Array 
# Dificuldade: Fácil
# Dado um array arr de tamanho n−1 que contém inteiros distintos no intervalo de 1 a n (inclusive),
# encontre o elemento faltante. O array é uma permutação de tamanho n com um elemento faltando.
# Retorne o elemento faltante.

def faltante(arr, n):
    aux = 1
    for i in range(n-1):
        if aux != arr[i]:
            return aux
        aux += 1
    return aux


# 2. Array Leaders 
# Dificuldade: Fácil
# Dado um array arr de n inteiros positivos, sua tarefa é encontrar todos os líderes no array. Um
# elemento do array é considerado um líder se ele for maior que todos os elementos à sua direita ou
# se for igual ao elemento máximo à sua direita. O elemento mais à direita é sempre um líder.

def lideres (arr, n):
    aux = []

    for i in range(n-1):
        elem = arr [i]
        flag = 0
        
        for j in range(1+i, n):
            if arr[j] > elem:
                flag = 1
                continue
        
        if flag == 0:
            aux.append(elem)
    
    aux.append(arr[n-1])
    return aux


# 3. Second Largest 
# Dificuldade: Fácil
# Dado um array arr, retorne o segundo maior elemento distinto do array. Se o segundo maior
# elemento não existir, retorne -1.

def segundo_maior (arr):
    maior = arr[0]
    segundo_maior = -9999999
    flag = 0
    
    for i in range(1, len(arr)):
        if arr[i] > maior:
            segundo_maior = maior
            maior = arr[i]
            flag = 1
        if (arr[i] < maior) & (arr[i] > segundo_maior):
            segundo_maior = arr[i]
            flag = 1
    
    if flag == 1:
        return segundo_maior
    return -1

# 4. Kadane’s Algorithm 
# Dificuldade: Média
# Dado um array de inteiros arr[]. Encontre o subarray contíguo (contendo pelo menos um número)
# que tem a soma máxima e retorne sua soma.

def kadane (arr):
    soma = arr[0]
    
    for i in range(1, len(arr)):
        if (soma + arr[i]) > soma:
            soma = soma + arr[i]
            if (soma) < (arr[i]):
                soma = arr[i]
    return soma 

# 5. Indexes of Subarray Sum 
# Dificuldade: Média
# Dado um array não ordenado arr de tamanho n que contém apenas inteiros não-negativos, encontre um subarray (elementos cont´ınuos) que tenha soma igual a s. Você deve retornar os ´ındices
# esquerdo e direito (indexa¸c˜ao baseada em 1) desse subarray.
# No caso de m´ultiplos subarrays, retorne os ´ındices do subarray que aparece primeiro ao mover da
# esquerda para a direita. Se nenhum subarray existir, retorne um array contendo o elemento -1.

if __name__ == '__main__':
    print('Teste dos exercícios:\n')

    print('EXERCÍCIO 1:')
    
    l = [1,2,3,5]
    l1 = [1]
    l2 = [1,2,3,4,5,6,8]
    l3 = [2,3,4,5,6,7]

    print(faltante(l, 5))
    print(faltante(l1, 2))
    print(faltante(l2, 8))
    print(faltante(l3, 7))

    print('---------------------------------------------------------------------------')

    print('EXERCÍCIO 2:')

    print(lideres([16,17,4,3,5,2],6))
    print(lideres([10,4,2,4,1],5))
    print(lideres([1,2,3,4,5,6,7,8,9,10],10))
    print(lideres([9,8,7,6,5,4,3,2,1,0],10))

    print('---------------------------------------------------------------------------')

    print('EXERCÍCIO 3:')

    print(segundo_maior([12,35,1,10,34,1]))
    print(segundo_maior([10,10]))
    print(segundo_maior([88,95, 10, 15]))
    print(segundo_maior([88,100, 95, 10, 15]))

    print('---------------------------------------------------------------------------')

    print('EXERCÍCIO 4:')

    print(kadane([1,2,3,-2,5]))

    print('---------------------------------------------------------------------------')

    print('EXERCÍCIO 5:')
    print('---------------------------------------------------------------------------')
    
