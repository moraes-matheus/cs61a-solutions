def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    
    result = 1
    i = 0 
    while i < k:
        result *= n - i
        i += 1
    return result

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    value = y
    num_digits = 1
    while value > 10:
        value = value // 10
        num_digits += 1
    value = y
    sum = 0
    while num_digits >= 0:
        size = 10 ** num_digits
        remainder = value // size
        sum += remainder
        value -= remainder * size
        num_digits -= 1
    return sum

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    num_digits = 0
    val = n
    while val > 10:
        num_digits += 1
        val //= 10

    val = n
    islast_eight = False
    while num_digits >= 0:
        digit = val // (10 ** num_digits)
        val -= digit * (10 ** num_digits)
        num_digits -= 1
        iseight = digit == 8
        if iseight and islast_eight:
            return True
        islast_eight = iseight
    return False