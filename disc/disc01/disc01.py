# python3 -m doctest -v disc01.py

# 1.1
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    return temp < 60 or raining

# 1.2
# When square is applied, it needs to evaluate all its parameters.
# Doing so, we call so_slow with value 5 as a parameter.
# But inside it as x will never be smaller than 0, an infinite loop is created.
# This way the program can't evaluate so_slow to continue evaluating square.
# Even if num was <= 0, the program would crash as it would try to do division by zero.

# 1.3
def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True