def sum_even_fib(n):
    a, b = 0, 1
    sum = 0
    while b < n:
        if b % 2 == 0:
            sum += b
        a, b = b, a+b
    return sum

if __name__ == '__main__':
    print(sum_even_fib(4e6))
