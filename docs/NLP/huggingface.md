# ?

## 下载地址

如果在服务器上直接git clone，就会要不断地下载所用的model，导致内存的浪费。需要指定一个“绝对”地址，这样就可以重用下载的模型。

1. 每次都传入参数`cache.dir`

    ```python
    from transformers impoet AutoModel
    AutoModel.from_pretrained(, cache_dir='')
    ```

2. 设系统变量`TRANSFORMERS_CACHE`

[修改huggingface transformers默认缓存文件夹](https://blog.csdn.net/zp_stu/article/details/126410323)
:https://blog.csdn.net/yuezhi
