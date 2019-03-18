def sum_array(arr):
    '''Return sum of all items in array.
    Args:
        arr (array): list or array-like object containing numerical values.
    Returns:
        float or int: sum of all elements in array.
    Examples:
        >>> sum_array([8, 3, 2, 7, 4])
        24
        >>> sum_array([3.2, 6.5, 7.0])
        16.7
    '''

    if len(arr) == 0:
        return 0
    else:
        return arr[-1] + sum_array(arr[:-1]) #Sum of last and prior to last elements.


def fibonacci(n):
    '''Return nth term in fibonacci sequence.
    Args:
        n (int): term in sequence to calculate.
    Returns:
        int: calculated term, equal to sum of previous two terms.
    Examples:
        >>> fibonacci(7)
        13
        >>> fibonacci(12)
        144
    '''

    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)  #Calculate fibonacci term from preceding terms.


def factorial(n):
    '''Return n!
    Args:
        n (int): number to calculate factorial from.
    Returns:
        int: factorial product.
    Examples:
        >>> factorial(5)
        120
        >>> factorial(9)
        362880
    '''
    if n == 1:
        return n
    else:
        return n * factorial(n-1) #Number multiplied to previous number.


def reverse(word):
    '''Return word in reverse.
    Args:
        word (str): word to reverse.
    Returns:
        str: reversed word.
    Examples:
        >>> word('cat')
        'tac'
        >>> word('flower')
        'rewolf'
    '''

    if word == '':
        return word
    else:
        return word[-1] + reverse(word[:-1]) #Prior to last character appended to last character.
