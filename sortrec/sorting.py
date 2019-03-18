def bubble_sort(items):
    '''Return array of items, sorted in ascending order.
    Args:
        items (array): list or array-like object to sort.
    Returns:
        array: list or array-like object to sorted in acsending order.
    Examples:
        >>> bubble_sort([3, 6, 3, 5, 8, 1])
        [1, 3, 3, 5, 6, 8]
        >>> bubble_sort(['bee', 'fly', 'mozzi', 'bug'])
        ['bee', 'bug', 'fly', 'mozzi']
    '''

    end = len(items) - 1

    while end != 0:

        #Check and swap element by element.
        for i in range(end):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]

        end = end - 1

    return items


def merge_sort(items):
    '''Return array of items, sorted in ascending order.
    Args:
        items (array): list or array-like object to sort.
    Returns:
        array: list or array-like object to sorted in acsending order.
    Examples:
        >>> merge_sort([3, 6, 3, 5, 8, 1])
        [1, 3, 3, 5, 6, 8]
        >>> merge_sort(['bee', 'fly', 'mozzi', 'bug'])
        ['bee', 'bug', 'fly', 'mozzi']
    '''

    length = len(items)
    if length == 1:
        return items

    mid = length // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])

    ordered = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            ordered.append(left[0])
            del left[0]
        else:
            ordered.append(right[0])
            del right[0]

    if len(left) == 0:
        ordered = ordered + right

    if len(right) == 0:
        ordered = ordered + left

    return ordered


def quick_sort(items):
    '''Return array of items, sorted in ascending order.
    Args:
        items (array): list or array-like object to sort.
    Returns:
        array: list or array-like object to sorted in acsending order.
    Examples:
        >>> quick_sort([3, 6, 3, 5, 8, 1])
        [1, 3, 3, 5, 6, 8]
        >>> quick_sort(['bee', 'fly', 'mozzi', 'bug'])
        ['bee', 'bug', 'fly', 'mozzi']
    '''

    length = len(items)

    if length <= 1:
        return items

    check = items[-1]

    less = []
    more = []
    equal = []

    #Compare to check and organise accordingly
    for i in items:
        if i < check:
            less.append(i)
        elif i > check:
            more.append(i)
        elif i == check:
            equal.append(i)

    less = quick_sort(less)
    more = quick_sort(more)

    return less + equal + more
