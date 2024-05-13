# utils

## GPU

!!! p 某某神经网络参数量有多少，大概占用多大的显存

Estimating neural network memory consumption
● Mini-batch sizes and gradient splitting trick
● Estimating neural network computation (FLOP/s)
● Calculating effective aperture sizes

<div class="grid" markdown>
<p><b>Training time</b><br>Memory to store outputs of intermediate layers (forward pass)<br>Memory to store parameters(<mark>model size</mark>)<br>Memory to store error signal at each neuron<br>Memory to store gradient of parameters<br>Any extra memory needed by optimizer (e.g. for momentum)</p>
<p><b>Test time</b><br>Memory to store outputs of intermediate layers (forward pass)<br>Memory to store parameters</p>
</div>

![](./pics/Memonry_2.webp)
![](./pics/Memonry_1.webp)

### Model size

> CNN
>
> !!! danger "per sample"
> ![](./pics/model_size_1.webp){width=80%}
>
> !!! p "一个 filter 的深度(通道数)要和 input 的深度(通道数)一样"
> ==model size==
> 从下往上：
> Conv1: 32 个 filters \* ((3 \* 3 weight \* 1 depth)  + 1 bias)  per filter = 320
> Conv2: 32 个 filters \* ((3 \* 3 weight \* 32 depth) + 1 bias) per filter = 9248
> Fnn1: ((14 \* 14) \* 32 weight \* + 1 bias) per layer \* 128 layers = 802944
> Fnn2: (128 weights + 1 bias) per layer\* 10 layers = 1290
> Total = 320 + 9248 + 802944 + 1290 = 813804
> If use 32-bit float : $813804\times4 \text{(bytes/float32)} \div1024\div1024\approx3.10M$
> ==intermedia output(parse layer)==
> Input: 28W \* 28H \* 1D = 
> after Conv1: 28W \* 28H \* 32D = 25088
> after Conv2: 28W \* 28H \* 32D = 25088
> after Maxpool： 14W \* 14H \* 32D = 6272
> after Fnn1: 128
> after Fnn2: 10 = output

### optimization





**GPU momory size:**

- GTX 980: 4GB
- Tesla K40: 12GB
- Tesla K20: 5GB


**Refernce:**

- [Memory usage and computational considerations]
- 


[Memory usage and computational considerations]:https://imatge-upc.github.io/telecombcn-2016-dlcv/slides/D2L1-memory.pdf