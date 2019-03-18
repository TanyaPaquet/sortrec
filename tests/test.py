from sortrec import recursion, sorting

def test_sum_array():
    """
    test that sum_array works correctly
    """

    assert recursion.sum_array([8, 3, 2, 7, 4]) == 24, 'incorrect'
    assert recursion.sum_array([3.2, 6.5, 7.0]) == 16.7, 'incorrect'


def test_fibonacci():
    """
    test that fibonacci works correctly
    """

    assert recursion.fibonacci(7) == 13, 'incorrect'
    assert recursion.fibonacci(12) == 144, 'incorrect'


def test_factorial():
    """
    test that factorial works correctly
    """

    assert recursion.factorial(5) == 120, 'incorrect'
    assert recursion.factorial(9) == 362880, 'incorrect'


def test_reverse():
    """
    test that reverse works correctly
    """

    assert recursion.reverse('cat') == 'tac', 'incorrect'
    assert recursion.reverse('flower') == 'rewolf', 'incorrect'


def test_bubble_sort():
    """
    test that bubble_sort works correctly
    """

    assert sorting.bubble_sort([3, 6, 3, 5, 8, 1]) == [1, 3, 3, 5, 6, 8], 'incorrect'
    assert sorting.bubble_sort(['bee', 'fly', 'mozzi', 'bug']) == ['bee', 'bug', 'fly', 'mozzi'], 'incorrect'


def test_merge_sort():
    """
    test that merge_sort works correctly
    """

    assert sorting.merge_sort([3, 6, 3, 5, 8, 1]) == [1, 3, 3, 5, 6, 8], 'incorrect'
    assert sorting.merge_sort(['bee', 'fly', 'mozzi', 'bug']) == ['bee', 'bug', 'fly', 'mozzi'], 'incorrect'


def test_quick_sort():
    """
    test that quick_sort works correctly
    """

    assert sorting.quick_sort([3, 6, 3, 5, 8, 1]) == [1, 3, 3, 5, 6, 8], 'incorrect'
    assert sorting.quick_sort(['bee', 'fly', 'mozzi', 'bug']) == ['bee', 'bug', 'fly', 'mozzi'], 'incorrect'
