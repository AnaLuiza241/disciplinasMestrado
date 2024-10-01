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



