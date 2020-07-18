def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


num = int(input('pls input an integer: '))
result = factorial(num)

print(f'{num} factorial is {result}')
