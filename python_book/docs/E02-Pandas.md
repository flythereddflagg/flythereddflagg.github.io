# E2 - Pandas

It's time to learn the basics of Pandas! Pandas is a powerful tool for data analysis and manipulation. The power of Pandas is centered around two classes: the Series class and the DataFrame class.

## A Basic Series

Lets try using the Series class. The following exercise will get your feet wet (I recommend you do these exercises in a Jupyter notebook).

```python
# In Jupyter:
# In[1]:
import pandas as pd
# In[2]:
input_data = [3,2,5.0,36,23.342,34,53.3]
the_series = pd.Series(data=input_data)
the_series
# Out[2]:
"""
0     3.000
1     2.000
2     5.000
3    36.000
4    23.342
5    34.000
6    53.300
dtype: float64
"""
```

As you can see, the Series is a lot like a list. But it is also like a dictionary. In the output, there is a column of index values that act as keys that map to the various values. Therefore, using one of the Series' methods for sorting you get the following:

```python
# In[3]:
the_series.sort_values()
# Out[3]:
"""
1     2.000
0     3.000
2     5.000
4    23.342
5    34.000
3    36.000
6    53.300
dtype: float64
"""
```

Notice how the values are now in order but the index-value paring is preserved (i.e. now the index column is out of order). In fact, we can make a series that has an arbitrary index as follows:

```python
# In[4]:
another_series = pd.Series(
    data=input_data, 
    index=['n cheeses', "spam", 32, "the number 36", "ohh a real float!", 22.2, "the last num"]
)
another_series
# Out[4]:
"""
n cheeses             3.000
spam                  2.000
32                    5.000
the number 36        36.000
ohh a real float!    23.342
22.2                 34.000
the last num         53.300
dtype: float64
"""
```



## A Basic DataFrame

## Loading Data

### CSV

### Microsoft Excel

### SQL



## Plotting Data

