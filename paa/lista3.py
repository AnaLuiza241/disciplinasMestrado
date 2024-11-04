# 1. Print 1 to n without using loops.
def print1toN (n):
    if n > 1:
        print1toN(n-1)
    print(n)

# 2. Print N to 1 without loop.
def printNto1 (n):
    print(n)
    if n > 1:
        printNto1(n-1)
        
# 3. Mean of an Array using Recursion.
def soma (arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    return arr[0] + soma(arr[1:])

def media (arr):
    n = len(arr)
    return soma(arr) / n

def mediav2(arr, soma=0, n=0):
    if len(arr) == 0:
        return (soma/n)
    soma = soma + arr[0]
    n = n + 1
    return mediav2(arr[1:], soma, n)

# 4. Sum of natural numbers using recursion.
def somaN (n):
    if n == 1:
        return 1
    return n + somaN(n-1)

# 5. Decimal to binary number using recursion.
def decimalToBinario (n):
    if (n // 2) == 0:
        return [n % 2]
    return decimalToBinario(n // 2) + [n % 2]

# 6. Sum of array elements using recursion.
def soma (arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    return arr[0] + soma(arr[1:])

# 7. Print reverse of a string using recursion.
def reverseString (str):
    if str == '':
        return
    reverseString(str[1:])
    print(str[0], end='')

# 8. Program for length of a string using recursion.
def lenString (str):
    if str == '':
        return 0
    return 1 + lenString(str[1:])

# 9. Sum of digits of a number using recursion.
def somaDigitos (n):
    if n < 10:
        return (n % 10)
    return (n % 10) + somaDigitos(n // 10)

# 10. Tail recursion to calculate sum of array elements.
def soma (arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + soma(arr[1:])

# 11. Program to print first n Fibonacci Numbers.
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

def printFibo(n):
    if n >= 0:
        printFibo(n-1)
        print(fibonacci(n), end=" ")

def printFibov2(n, nm2=0, nm1=1):
    if n >= 0:
        print(nm2, end=' ')
        printFibov2(n-1, nm1, nm2+nm1)

# 12. Programa para fatorial de um número.
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)

# 13. Programas Recursivos para encontrar os elementos Mínimos e Máximos de um vetor.
def maximo(arr, max=float('-inf')):
    if arr == []:
        return max
    if arr[0] > max:
        max = arr[0]
    return maximo(arr[1:], max)

def minimo(arr, min=float('inf')):
    if arr == []:
        return min
    if arr[0] < min:
        min = arr[0]
    return minimo(arr[1:], min)

# 14. Função recursiva para verificar se uma string é um palíndromo.
def ehPalindromo(str):
    if not str:
        return True
    i = str[0]
    f = str[-1]
    if i == f:
        return ehPalindromo(str[1:-1])
    return False

# 15. Imprimir a Série de Fibonacci em ordem inversa usando Recursão.
def printFiboInverso(n, nm2=0, nm1=1):
    if n > 0:
        printFiboInverso(n-1, nm1, nm2+nm1)
        print(nm2, end=' ')

# 17. Busca Binária usando Recursão.
def buscaBinaria(arr, alvo, inicio=0):
    if not arr :
        return -1
    n = len(arr)
    i = n//2
    meio = arr[i]
    if meio == alvo:
        return i + inicio
    if meio < alvo:
        return buscaBinaria(arr[i + 1:], alvo, inicio + i + 1)
    else:
        return buscaBinaria(arr[0:i], alvo, inicio)

if __name__ == '__main__':
    print('Teste dos exercícios:\n')

    print('EXERCÍCIO 1:')
    print1toN(5)
    print()

    print('EXERCÍCIO 2:')
    printNto1(8)
    print()

    print('EXERCÍCIO 3:')
    print(media([1, 2, 3, 4, 5]))
    print(mediav2([1, 2, 3, 4, 5]))
    print(media([10, 20, 30, 40, 50]))
    print(mediav2([10, 20, 30, 40, 50]))
    print(media([1]))
    print(mediav2([1]))
    print()

    print('EXERCÍCIO 4:')
    print(somaN(5))
    print(somaN(10))
    print(somaN(1))
    print()

    print('EXERCÍCIO 5:')
    print(decimalToBinario(10))
    print(decimalToBinario(15))
    print(decimalToBinario(165))
    print()

    print('EXERCÍCIO 6:')
    print(soma([1, 2, 3, 4, 5]))
    print(soma([10, 20, 30, 40]))
    print(soma([5]))
    print()

    print('EXERCÍCIO 7:')
    reverseString('hello')
    print()
    reverseString('recursion')
    print()
    print()

    print('EXERCÍCIO 8:')
    print(lenString('hello'))
    print(lenString('recursion')) 
    print()

    print('EXERCÍCIO 9:')
    print(somaDigitos(1234))
    print(somaDigitos(9876))
    print(somaDigitos(10))
    print()

    print('EXERCÍCIO 10:')
    print(soma([1, 2, 3, 4]))
    print(soma([5, 10, 15, 20]))
    print()

    print('EXERCÍCIO 11:')
    printFibo(5)
    print()
    printFibov2(5)
    print()
    printFibo(7)
    print()
    printFibov2(7)
    print()

    print('EXERCÍCIO 12:')
    print(fatorial(5))
    print(fatorial(0))
    print(fatorial(1))
    print(fatorial(7))
    print()

    print('EXERCÍCIO 13:')
    print(f'Entrada: [1, 4, 3, -5, 10]   Máximo: {maximo([1, 4, 3, -5, 10])}   Mínimo: {minimo([1, 4, 3, -5, 10])}')
    print()
    
    print('EXERCÍCIO 14:')
    str='radar'
    print(f'{str} é palindromo? {ehPalindromo(str)}')
    print()

    print('EXERCÍCIO 15:')
    printFiboInverso(15)
    print()

    print('EXERCÍCIO 16: Não consegui ')
    print()

    print('EXERCÍCIO 17:')
    print(buscaBinaria([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))



