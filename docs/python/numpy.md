# Numpy & Scipy

for ==scientific computing==  in Python，provide ==multidimensional array object==

==Numpy== 实现了 多维同质数组 multidimensional homogenous array & 矩阵。不仅能处理数字还可以存放其它由用户定义的记录。

==Scipy== 是基于 Numpy 的一个库，转为线性代数、数值积分、统计学设计，。

## np.ndarray

!!! danger "shape & ndim, vector & matrix"
    ||Vector|Matrix|
    |--|--|--|
    `a.shape`|(3,) or (, 3)|(3, 1) or (1, 3)|
    `a.ndim`|1|2

!!! danger "默认是 float 类型"

!!! p "`Int index` & `slice`"
    - `slice`
        是==原来的subarray==， 相对顺序不会变化
    - `Int index`
        任意构成，只是数据存在，但是相对顺序会变化的。
    ```python hl_lines="2 6"
    a = np.array([[1, 2], [3, 4]])
    a[[1, 0],[1, 0]]
    # >>> array([4, 1]) 与原来的相对不一样了
    # = np.array([a[1][1],
    #             a[0][0]])ß
    a[[[1, 0],[1, 0]],[[1, 0],[1, 0]]]
    # >>> array([[4, 1],[4, 1]]) 只是取自数据
    # = np.array([[a[1][1], a[0][0]],
    #            [a[1][1], a[0][0]]])
    ```

|case|code||
|--|--|--|
|创建<br> shape = `Int` or <br>`Tuple(shape1, shape2, ...)` |`np.array(list[list[...]])`||
|^|`np.zeros(shape)`|全0|
|^|`np.ones(shape)`|全1|
|^|`np.eye(shape)`|单位矩阵|
|^|`np.full(shape, value)`|常数|
|^|`np.random.random(shape)`|任意|
|切片要单行或单列|`row = a[0, :]`, `col = a[:, 0]`|Int index ➡️ shape 要降级|
|^|`row = a[0:1, :]`, `col = a[:, 0:1]`| slice ➡️ shape 与原来的同级|

```python
""" create """
import numpy as np
a = np.eye(2)
# >>> a = array([[1., 0.],[0., 1.]])
a = np.full((2, 1), 7)
# >>> a = array([[7], [7]])
a = np.random.random((2, 1))
# >>> array([[0.5018725], [0.283335 ]])

""" 切片要单行或单列, 表示 vector  """
a = np.array([[1, 2, 3], [4, 5, 6]])
row1 = a[0, :]  # int index
row2 = a[0:1, :]  # slice
# >>> row1.shape = (3,) ; row2.shape = (1, 3)
col1 = a[:,0]
col2 = a[:,0:1]
# >>> col1.shape = (2,) ; col2.shape = (1, 2)
```

- numpy ↔️ image
    1. `img_array = opencv()` 来读取图片 自动是 `numpy.array`
    2. `img_array = np.array(img)`

## 操作

### 乘法

||`a*b`|`a.dot(b)`|
|--|--|--|
|?|对应位置相乘|矩阵内积<br> ==Matrix Product==|

```python
a = np.array([[1, 2], [3, 4]])
b = np.array([[1, 1], [2, 2]])
a * b 
# >>> array([[1, 2], [6, 8]])
a.dot(b)
# >>> array([[5, 5], [11, 11]])
```

!!! p "range:int  <br> np.arange float"
