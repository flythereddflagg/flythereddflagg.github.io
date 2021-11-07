# E3 - Numpy

Numpy is a Python library that allows complex math to be done easily. Generally, this library is ideal for performing linear algebra calculations and contains modules for common calculations. The following example should show this.

## Multiply Two Matrices

The definition of matrix multiplication is given here for reference.

*For two matricies $A$, $B$ with row-column dimensions $d,n$ and $n,f$ respectively, each element (noted by $r,c$ for each row and column) of the matrix product $C$ of $A$ and $B$ ($C = AB$​):*

$$C_{r,c} = \sum^n_i A_{r,i} \cdot B_{i,c}$$

Given this definition we will code this into a Python program without and then with Numpy.

```python
# np_matmul.py
import timeit # get the module for timing code
import numpy as np


def matmul(a, b):
    """
    Using built-in Python functions, multiply matricies
    a and b and return an new matrix c.
    """
    d, f, n = len(a), len(b[0]), len(b)
    c = [[0.0 for _ in range(f)] for __ in range(d)]

    for row in range(d):
        for column in range(f):
            for i in range(n):
                c[row][column] += a[row][i]*b[i][column]

    return c


def np_matmul(a, b):    
    """
    Using Numpy, multiply matricies
    a and b and return an new matrix c.
    We will use the special case of the @
    operator here.
    """
    return a @ b


# here are a and b, two matrices to be multiplied
a = [
    [2,3,4],
    [3,1,9],
    [4,1,4]
]
b = [
    [2],
    [6],
    [5]
]
# now pack these matrices into numpy array objects
a_array, b_array = np.array(a), np.array(b)

# lets compare the two calculations by running them 10000 times
n_times = 10_000
t_matmul = timeit.timeit(lambda: matmul(a,b), number=n_times)
t_npmatmul = timeit.timeit(
    lambda: np_matmul(a_array, b_array), 
    number=n_times
)
pct_improvement = (1 - (t_matmul - t_npmatmul)/t_matmul) * 100

print(f"""
% improvement : {pct_improvement:.0f}
time python   : {t_matmul:.3f}
time numpy    : {t_npmatmul:.3f}
""")
```

This should produces qualitatively similar results to this:

```
> python np_matmul.py

% improvement : 37
time python   : 0.066
time numpy    : 0.024

```

This shows how much faster Numpy is than plain Python. We will talk about the reason that this is but for now lets look at some other powerful things we can do with Numpy arrays.

