# sortrec
The sortrec package contains recursive functions for calculating the sum of array-like object elements, Fibonacci sequence terms, factorials, and reversing the order of elements in an array-like object. A selection of sorting functions is also included.

## Building this package locally
`python setup.py sdist`

## Installing this package from GitHub
`pip install git+https://github.com/TanyaPaquet/sortrec.git`

## Updating this package from GitHub
`pip install --upgrade git+https://github.com/TanyaPaquet/sortrec.git`

## Usage
```python
from sortrec import recursion

recursion.sum_array([8, 3, 2, 7, 4]) # returns 24
recursion.fibonacci(7) # returns 13
recursion.factorial(5) # returns 120
recursion.reverse('flower') # returns 'rewolf'
```
```python
from sortrec import sorting

sorting.bubble_sort([3, 6, 3, 5, 8, 1]) # returns [1, 3, 3, 5, 6, 8]
sorting.merge_sort([3, 6, 3, 5, 8, 1]) # returns [1, 3, 3, 5, 6, 8]
sorting.quick_sort([3, 6, 3, 5, 8, 1]) # returns [1, 3, 3, 5, 6, 8]
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
