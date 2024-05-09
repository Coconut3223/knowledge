# 笔面

## 排序

!!! danger "input: 无序的数组 & k:int<br>output：数组第k大的元素<br> 优化 & 时间复杂度"

```python
def method(lst, k:int):
    if k > len(lst) or k < 1:
        return f'{k} is less than the length of list'
    return sorted(lst)[k-1]

if __name__ == '__main__':
    lst = [3,1,5,4,2]
    print(method(lst, k=3))
```

!!! danger "子列表的第一个列表排序"

``` title="data"
data = [['a', 10,'2020/12/1'],
        ['b', 2, '2020/12/2'],
        ['a', 5,'2020/12/1'],
        ['c', 21,'2020/12/4'],
        ['b', 19, '2020/12/1'],
        ['c', 5, '2020/12/6'],
        ['c', 1, '2020/12/7'],
        ['a', 8, '2020/12/2'],
        ['a', 8, '2020/12/3']]
```

``` python
def func1(data):
    return sorted(data, key=lambda x:x[0])
#print(func1(data))
```

!!! danger "子列表第2个元素分组求和"

```python
def func2(data):
    user_set = set(x[0] for x in data)
    res = []
    for user in user_set:
        print(sum(x[1] for x in data if x[0]==user))
        if sum(x[1] for x in data if x[0]==user) > 40:
            res.append(user)
    return res
```

!!! danger "子列表第一个元素分组求最高"

``` python
def func3(data):
    # res = dict()

    # for rec in data:
    #     if rec[0] not in res.keys():
    #         res[rec[0]] = (rec[1], rec[2])
    #     elif rec[1] > res[rec[0]][0]:
    #         res[rec[0]] = (rec[1], rec[2])
    # return res
    user_payment_dict = {}
    for entry in data:
        username = entry[0]
        payment = entry[1]
        payment_time = entry[2]

        if username in user_payment_dict:
            if payment > user_payment_dict[username][0]:
                user_payment_dict[username] = (payment, payment_time)
        else:
            user_payment_dict[username] = (payment, payment_time)

    return user_payment_dict

# user_department
# u
print(func3(data))
```
