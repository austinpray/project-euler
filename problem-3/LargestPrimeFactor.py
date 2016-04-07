from math import ceil, sqrt

def get_prime_factors(n):
    # base case
    if n <= 1:
        return []
    # https://www.python.org/dev/peps/pep-0289/
    # https://wiki.python.org/moin/Generators
    # Do not look beyond sqrt of n because there won't be any candidates after that
    prime = next((x for x in range(2, ceil(sqrt(n))+1) if n % x == 0), n)
    # // is integer division in python 3
    return [prime] + get_prime_factors(n//prime)


def get_largest_prime_factors(n):
    return max(get_prime_factors(n))
