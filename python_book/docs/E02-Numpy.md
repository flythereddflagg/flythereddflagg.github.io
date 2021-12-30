<!-- Navigation -->

---

[Previous: E01 - Getting Started Again](./E01-Getting-Started-Again.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: E03 - Pandas ](./E03-Pandas.md)

---
<!-- End Navigation -->
# E3 - Numpy

This is a shorter section because there is less to explain. At the conclusion of this section, I will refer you to the official Numpy documentation because its way better than this book. (Trust me.) With that said, this should be a nice little introduction to get your feet wet.

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

## More `numpy` in Jupyter

The following is an exercise to be done in Jupyter (but you can just do it in Python too).

`In[]:`

```python
# do this in a Jupyter notebook
# if you do this in a Python script,
# replace all calls to "display"
# with print
import numpy as np
```

`In[]:`


```python
# we will start with two arrays
a = np.array([
    [21, 42, 32],
    [1, -129.2, 234.0],
    [3, 6, 9]
])
# make a 3X3 array of zeros
b = np.zeros((3,3)) 
display(a)
display(b)
```

`Out[]:`


    array([[  21. ,   42. ,   32. ],
           [   1. , -129.2,  234. ],
           [   3. ,    6. ,    9. ]])
    array([[0., 0., 0.],
           [0., 0., 0.],
           [0., 0., 0.]])

`In[]:`

```python
# notice that arrays are forced
# to be all the same data type
display(a.dtype, b.dtype)
```

`Out[]:`


    dtype('float64')
    dtype('float64')

`In[]:`

```python
# we can do element-wise math
display(b + 1)
display(a / 100)
display((b + 1) + a)
```

`Out[]:`


    array([[1., 1., 1.],
           [1., 1., 1.],
           [1., 1., 1.]])
    array([[ 0.21 ,  0.42 ,  0.32 ],
           [ 0.01 , -1.292,  2.34 ],
           [ 0.03 ,  0.06 ,  0.09 ]])
    array([[  22. ,   43. ,   33. ],
           [   2. , -128.2,  235. ],
           [   4. ,    7. ,   10. ]])

`In[]:`

```python
# we can do linear algebra calculations like determinants
# inverse matrices or solvers
display(np.linalg.det(a))
display(np.linalg.inv(a))
display(a @ np.linalg.inv(a)) # to prove it is the inverse

# get the first column of b+1
display(np.linalg.solve(a, (b + 1)[:,1])) 
```

`Out[]:`


    -12201.60000000001
    array([[ 0.21036585,  0.0152439 , -1.14430894],
           [-0.05679583, -0.00762195,  0.40011146],
           [-0.03225806,  0.        ,  0.22580645]])
    array([[ 1.0000000e+00,  0.0000000e+00, -8.8817842e-16],
           [ 8.8817842e-16,  1.0000000e+00,  0.0000000e+00],
           [ 0.0000000e+00, -6.9388939e-18,  1.0000000e+00]])
    array([-0.91869919,  0.33569368,  0.19354839])

## The Numpy Manual

This is one area where I have to admit that the developers of Numpy do a much better job of explaining their software than I ever could. Therefore I am going to refer you to the [Numpy Manual](https://numpy.org/doc/stable/) for further reading. The main thing I want you to get out of these exercises is the following:

- Numpy can do all sorts of powerful mathematical calculations with fewer lines of code than Python alone.
- Numpy can do these calculations *much* faster than Python alone (37% faster on my computer).
- You should use Numpy for calculations involving matrices and element-wise calculations.
- Numpy software is designed to integrate with Scipy, Pandas, and other STEM-focused libraries.


<!-- Navigation -->

---

[Previous: E01 - Getting Started Again](./E01-Getting-Started-Again.md) | [Table of Contents](./00-Table-of-Contents.md) | [Next: E03 - Pandas ](./E03-Pandas.md)

---
<!-- End Navigation -->
