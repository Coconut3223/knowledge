# ?

## 方法下载

!!! p "来自[如何快速下载huggingface模型——全方法总结]的推荐"
    Linux/Mac OS/windows 默认推荐使用huggingface-cli，对外网连接较好（丢包少）的时候，可尝试 huggingface-cli+hf_transfer（可选）。
    网络连接不好，推荐先GIT_LFS_SKIP_SMUDGE=1 git clone，其次再对大文件用第三方、成熟的多线程下载工具，Linux 推荐hfd脚本+aria2c，Windows 推荐 IDM。用第三方工具的好处是，下载上百GB的模型、数据集，你可以放个一晚上，第二天就下载好了，而不是第二天早晨发现下载了10%断了还得继续。
    偶尔小文件下载，直接访问镜像站，用浏览器下载。

!!! warning "目前没用到很大的模型，所以用snapshot_download enough"

### 直接 `from_pretrained`

如果在服务器上直接git clone，就会要不断地下载所用的model，导致内存的浪费。需要指定一个“绝对”地址，这样就可以重用下载的模型。

自动下载到 <kbd>root/.cache/huggingface/transformers</kbd>

1. 每次都传入参数`cache_dir`

    ```python
    from transformers impoet AutoModel
    AutoModel.from_pretrained(, cache_dir='')
    ```

2. 设系统变量`TRANSFORMERS_CACHE`

[修改huggingface transformers默认缓存文件夹](https://blog.csdn.net/zp_stu/article/details/126410323)

### `snapshot_download` 【推荐】

downloads an entire repository at a given revision.

默认下载最新的版本，如果要指定版本，传 `revision=specific_version`

可以通过 `allow_patterns` | `ignore_patterns` 来指定或排除特定文件下载

local_dir must be a path to a folder on your system.

支持断点续传、多线程、指定路径、配置代理、排除特定文件等功能。然而有两个缺点：

1. 该方法依赖于 transformers 库，而这个库是个开发用的库，对于自动化运维有点重；
2. 该方法调用比较复杂，参数较多，例如默认会检查用户缓存目录下是否已有对应模型，如已有则会创建符号链接，不理解的容易导致问题。

```cmd
pip install huggingface_hub
```

```python title="download.py"
# if need login in
import huggingface_hub
huggingface_hub.login('HF_token')
# token 从 https://huggingface.co/settings/tokens 获取

from huggingface_hub import snapshot_download
snapshot_download(  # download model
    repo_id='google/mt5-base',  # model在HF的路径
    local_dir='./model/'  # 要下载的位置
)

snapshot_download(  # download dataset
    repo_id='google/fleurs',  # model在HF的路径
    repo_type='dataset'
    local_dir='./data/'  # 要下载的位置
)
```

```python title="load.py"
local_path = './model/'
model = AutoModel.from_pretrained(local_path)
```

### 模型需要许可

!!! warning "怎么看模型是否需要许可"
    如果在模型主页 **Files and versions** 看不到模型文件，那就是需要申请许可通过才能下载的 ==Gated Model==。

申请通过后，就可以**在模型主页的 Files and versions 中看到模型文件了**，浏览器的话直接点击下载即可。但是如果想要用工具例如 huggingface-cli 下载，则需要获取 access token:

访问[huggingface.setting.token 管理页]，选择 New 一个 token，只需要 Read 权限即可，创建后便可以在工具中调用时使用了。

[下载huggingface-transformers模型至本地，并使用from_pretrained方法加载]
[Download files from the Hub]

[下载huggingface-transformers模型至本地，并使用from_pretrained方法加载]:https://blog.csdn.net/weixin_44612221/article/details/129884741
[如何快速下载huggingface模型——全方法总结]:https://www.yunqiic.com/2024/01/04/%E5%A6%82%E4%BD%95%E5%BF%AB%E9%80%9F%E4%B8%8B%E8%BD%BDhuggingface%E6%A8%A1%E5%9E%8B-%E5%85%A8%E6%96%B9%E6%B3%95%E6%80%BB%E7%BB%93/
[huggingface.setting.token 管理页]: https://huggingface.co/settings/tokens
[Download files from the Hub]:https://huggingface.co/docs/huggingface_hub/v0.13.3/guides/download
