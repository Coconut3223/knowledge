# Enhanced Python

## Script & Module & Package

==script 脚本==。是一个包含可执行代码的文件，一个 py 文件，更多时候是指可以直接运行的 py 文件。为一个特定任务写成。
==顶层代码==。由用户指定的最先开始运行的那一个 py 文件，是应用程序的入口点。**它的`__name__` 被设为 `__main__`**
==module 模块==。主要是被引用，包含了**相关性较高**的程式码。
==package 包==。包含了一个或多个的 Module ，并且拥有 `__init__.py`
==library 库==。

### 顶层代码

==顶层代码==。由用户指定的最先开始运行的那一个 py 文件，是应用程序的入口点。

!!! p "顶层代码的`__name__` 被设为 `__main__`。"
    module 如果是 被 import，它的 `__name__` 就会是它自己名字；如果是以**脚本方式执行**，会把 `__name__ = "__main__"`
    ``` title="dir"
    + A
        A1.py
        A2.py
        + subA
            a1.py
    ```

    ```python title="A1.py"
    print(f'in A1: {__name__}')
    ```

    ``` python title="A2.py"
    from A1 import *
    from subA.a1 import *
    print(f'in A2: {__name__}')
    ```

    ```python title="a1.py"
    print(f'in a1: {__name__}')
    ```
    运行 `python A2.py`， A2 是被运行的顶层代码， A1 & a1 时被 import 的module
    ```python
    # >>> in A1: A1
    # >>> in a2: subA.a2  # 如果有上层，就会把上层文件也展示
    # >>> in A2: __main__  # A2 是被运行的顶层代码，被改为 `__main__`
    ```

    !!! p ""
        可以利用`if __name__ == '__main__':`来控制 **执行** 和 **被引用时** 的运行的代码内容。
        最好用 `main` 进行封装，再调用。如果直接放在 `if __name__ == '__main__':` 下的变量会成为**全局变量**。

!!! quote "`__main__.py` in package 参见 package section"

### Module

==module 模块==。主要是被引用，包含了**相关性较高**的程式码。

- 在**模块内部**，模块名 通过全局变量 `__name__` 获取.
- 每个模块都有自己的**私有命名空间**，它会被用作模块中定义的所有函数的全局命名空间。

### Package

==package 包==。包含了一个或多个的 Module ，并且拥有 `__init__.py`。

但是一个比较齐全的包是：

```python
"""
+ package
    __init__.py
    __main__.py
    module1.py
"""
```

#### `__init__.py`

!!! danger "需要有 `__init__.py` 文件才能让 Python 将包含该文件的目录当作包来处理"

从一个 package 里面调用东西的时候，`__init__.py` 的代码会**被首先执行**.
能帮助 package 完成 **批量导入和规范化导入**

!!! warning "其可见性的维护是靠一套需要大家自觉遵守的”约定“"
    [Python中的__all__]: 使用 `from xxx import *` 导入该文件时，只会导入 `__all__` 列出的成员，可以其他成员都被排除在外。
    但是直接定位到精确调用是可以的

    !!! p ""
        修改一个暴露的接口只修改一行，方便版本控制的时候看 diff
    ``` title="dir"
    + A
        __init__.py
        A1.py
        A2.py
        + subA
            a1.py
            __init___.py
    ```

    ```python title="subA.a1.py"
    def f1():
        print("F1")
    def f2():
        print("F2")
    ```


    ```python title="subA.__init__.py"
    # 在 package 级别暴露接口
    from sub.a1 import *
    __all__ = [
        "f1"
    ]
    ```
    在 package 级别暴露接口，module level 也类似。如果采用`from package import *`
    ```python title="A1.py"
    from subA import *
    f1()
    # >>> F1  # 成功了 
    f2()
    # >>> NameError: name 'f2' is not defined. Did you mean: 'f1'?
    ```
    如果采用 `from package.module import func` 精确调用
    ```python title="A2.py"
    from subA.a1 import f1, f2
    f1()
    # >>> F1
    f2()
    # >>> F2
    ```

#### `__main__.py`

`python -m package`。 使用 `-m` 从命令行直接调用软件包本身时，将执行 `__main__.py`。

`__main__.py` 的内容通常不会用 `if __name__ == '__main__'` 块围起来。相反，这些文件会保持简短**并从其他模块导入函数来执行。 这样其他模块就可以很容易地进行单元测试并可以适当地重用。**

!!! p "package 里的 module 的单元测试是在 `__main__.py` 进行。"

### import

为了**快速加载模块（不是加速执行）**，Python 把**模块的编译版本**缓存在 `__pycache__ dir` 中，文件名为 `module.version.pyc，version` 对编译文件格式进行编码
> CPython 的 3.3 发行版中，spam.py 的编译版本 == `__pycache__/spam.cpython-33.pyc`

!!! quote "为什么没有 运行脚本的已编译档案？"
    运行脚本 当作程式的进入点，所以每一次执行 `python xxx.py` 指令时，Python编译器都要进行编译，所以没有将 `xxx.py` 进行快取的动作。

#### 从内容区分

- `import module` = 调用 》 `module.specific_func()`
- `from module import specific_func` = 调用 》 `specific_func()`
- `from module import *` = 调用 》 `specific_func()`

!!! warning "尽量不要用 `from module import *`，这种方式向解释器导入了一批未知的名称，可能会覆盖已经定义的名称。"

!!! p "`from module import *` 会导入**所有不以下划线（_）开头**的名称。"

!!! danger ""
    - `from package import item` 时，item 可以是包的子模块（或子包），也可以是包中定义的函数、类或变量等其他名称。
    - `import item.subitem.subsubitem` 时，除最后一项外，**每个 item 都必须是包；最后一项可以是模块或包**，但不能是上一项中定义的类、函数或变量。

#### 从方式区分

See 路径相关的 section

- 绝对导入
- 相对导入

## 路径相关

!!! danger "如果不是从脚本所在路径 `python ./xxx.py` 运行脚本，就会有 working directory & script path 区别"
    用户在磁盘上寻找文件或子目录时，所历经的线路叫路径。
    目录和文件夹是一个意思

==工作目录 working directory cwd==。用户当前目录。`os.getcwd()`
==脚本路径 script path==。脚本文件所在的路径。 `__file__`
==系统路径 system path sys==。操作系统用来查找**可执行文件和库文件**的一组目录路径。`sys.path:List`

- 加入sys `sys.path.append(new_path)`
- 查看 `sys.path`

【process】

- 程序将<u>脚本所在的目录</u>加入到 <u>sys</u> 中，用来查找**可执行文件和库文件**
    `os.path.dirname(__file__) == sys.path[0]`
- 程序会实行<u>脚本里的代码</u>，在<u>cwd</u> 进行查找创造文件。

<div class="grid" style="grid-template-columns: repeat(3, 1fr) !important;" markdown>
``` title="dir"
+ A
    A1.py
    + subA
        a1.py
```


```python title="A1.py"
import os, sys

if __name__ == "__main__":
    print(f'working_directory = {os.getcwd()}')
    print(f'script_path = {__file__}' )
    print(f'system_path[0] = {sys.path[0]}')
    with open('1.txt', 'w'):
        ...
```

</div>


在 subA 底下运行 `A1.py` `.../python.exe .../A/A1.py`

```python
# >>> working_directory = ...\A\subA
# >>> script_path = ...\A\A1.py
# >>> system_path[0] = ...\A
# >>> 1.txt 在 subA 底下， # 在工作目录对应进行创建
```

### import - module 搜索路径

当 `import spam`，解释器：

1. 搜索 `spam` 的内置模块。这些模块的名称在 `sys.builtin_module_names` 中列出。
2. 如果未找到，它将在变量 `sys.path` 所给出的目录列表中搜索

**sys.path的初始化：**

- 被**命令行直接运行的脚本所在的目录**。
- PYTHONPATH （目录列表，与 shell 变量 PATH 的语法一样）。
- 依赖于安装的默认值（按照惯例包括一个 site-packages 目录，由 site 模块处理）。

!!! p  ""
    程序将<u>`run.py` 脚本所在的目录</u>加入到 <u>sys</u> 中，用来查找**可执行文件和库文件**

自己写的包注意 import 路径，从系统路径中能不能找到，能不能形成可到达的路径

1. 通过 `sys` 添加搜索路径 `sys.path.append('package path')`
2. 绝对引用。当包由多个子包构成时，可以使用绝对导入来引用**同级包的子模块**。
3. 相对引用。

!!! danger "主模块始终使用 <u>绝对导入</u>"
    相对导入基于当前模块名`module.__name__`。
    - 模块作为**顶层文件被执行**时，`__name__="__main__"`，不包含任何包的名字
    - 但作为**普通模块被 import**， 就会被包含包。

!!! p "绝对引用 & 相对引用"
<div class="grid" markdown>
```title="dir"
+ A
    A1.py
    A2.py
```

```python title="A1.py"
import A2  # 绝对引用
import .A2  # 相对引用
```

</div>

[import 问题浅谈]

## Others

- Magic Number 魔数（中性词）
   [编程中的「魔数」（magic number）是什么意思？平时我们能接触到哪些魔数？]
   一般是指**硬写到代码里的整数常量**，数值是编程者自己指定的，其他人不知道数值有什么具体意义，表示不明觉厉，就称作magic number。编程教材书用magic number指代**初学者不定义常量直接写数的不良习惯。**
  - **贬义词**: 指的是代码中出现的没有说明的数字。代码中突然出现一个没说明用途的数字会让其它阅读代码、维护代码的的人非常难受。
    > 例如写3.1416这种数字，也应该改为数学库中的π常数，例如Unity中的Mathf.PI。
  - **褒义词**: 通过一些底层原理实现骚操作
  - **中性词**：
    > . ELF文件头会写入一个magic number，检查这个数和自己预想的是否一致可以判断文件是否损坏。
    > . 如果你用16进制编辑器打开一个文件，它的开头不是FFD8FF，那就不是jpg文件。这个魔数一般会在相关文件标准中进行规定，所有人都要遵守

## Todo

[import雜談之三———sys.path的洪荒之時]

[import雜談之三———sys.path的洪荒之時]: https://ithelp.ithome.com.tw/articles/10196901
[Python中的__all__]:https://zhuanlan.zhihu.com/p/54274339
[import 问题浅谈]:https://zhuanlan.zhihu.com/p/69099185
[编程中的「魔数」（magic number）是什么意思？平时我们能接触到哪些魔数？]:https://www.zhihu.com/question/22018894
