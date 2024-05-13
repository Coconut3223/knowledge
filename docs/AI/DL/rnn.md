# Recurrent Neural Networks

## standard RNN

<kbd>Variable-length Sequene</kbd> <kbd>Sequential-Dependent</kbd> <kbd>Time-Dependent</kbd>

==recurrent==: **revisit or reuse past states as inputs** to predict the next or future states.

==Memory== 拥有前一个阶段的输出作为未来输出的灵感的一部分。

!!! p "The biggest difference between RNN and traditional neural networks is that each time the previous output is taken to the next hidden layer and trained together."

<div class="grid" markdown>
<figure markdown="span">![](./pics/RNN_6.gif)</figure>
<figure markdown="span">![](./pics/RNN_1.gif)</figure>
</div>
<p>最后只要 o5 进行解码</p>
<div class="grid" markdown>
<figure markdown="span">![](./pics/RNN_3.jpg){width=70%}<p>x1 进去产生 h1，h1 同时存到 m1, 此时 o1 完全是 h1 的解码<br> 为了统一，也可以自定义一个 m0 同样和 x1 进去产生 h1</p></figure>
<figure markdown="span">![](./pics/RNN_4.webp){width=70%}<p>x2 & m1 进去产生 h2, h2 同时被存到 m12， 此时 o2 完全是 h2 的解码</p></figure>
<figure markdown="span">![](./pics/RNN_5.jpg){width=70%}<p>x3 & m12 进去产生 h3, h3 同时被存到 m123， 此时 o3 完全是 h3 的解码 </p></figure>
<figure markdown="span">![](./pics/RNN_6.jpg){width=70%}<p>memory (m1,m12,...) 并不是直接raw input 进去产生新一轮的 hidden state (h2,h3,...), 而是采用一个<b>权值矩阵 W 参数化</b>记忆单元</p></figure>
</div>

$$s_t=\text{tanh}(Ux_t+Ws_{t-1})$$

### shortcoming

RNN 比较擅长解决 想要的信息 & 相关的信息 距离较近。

<div class="grid" markdown>
<figure markdown="span">![](./pics/RNN_8.png)<p>Good</p></figure>
<figure markdown="span">![](./pics/RNN_9.png)<p>Bad</p></figure>
</div>

<div class="grid" markdown>
<figure markdown="span">![](./pics/RNN_7.jpg)</figure>
<p>short-term memory has a large impact (such as the orange region), but long-term memory effects are small (such as black and green regions), which is the <b>short-term memory problem</b> of RNN.</p>
</div>
如果序列足夠長，它們將很難將資訊從較早的時間步驟傳遞到較晚的時間步驟。因此，如果您嘗試處理一段文字來進行預測，RNN 可能會從一開始就遺漏重要資訊。
1. RNN has short-term memory problems and cannot handle very long input sequences
2. Training RNN requires significant cost

![](./pics/RNN_2.jpg)

- <u>unfold</u>
- **数据是按照顺序进入**，我们在处理序列化的数据时，往往会在用**滑动窗口**的办法来调整不同的结构。
- m0 的设置：这个初始值可以作为一个参数进行反向传播，也可以将其简单的设置为零，表示前面没有任何信息。

!!! p "在同一层的隐藏单元中进行传播的 权值矩阵W & 输入到隐层的权值矩阵U & 隐层到输出的权值矩阵V，为什么是相同的?"
    就像是 CNN 用参数共享的卷积核来提取相同的特征，在RNN中，使用参数共享的 U,V 来**确保相同的输入产生的输出是一样**。参数共享的矩阵W **确保了对于相同的上文，产生相同的下文**。
    > 一段文本中，可能会出现大量的“小狗”。无论小狗出现在哪个位置（x?），参数共享使得神经网络在输入“小狗”的时候，在不考虑上下文的 memory，$x\xrightarrow{完全编码}h$ 的结果是一样。类似地，在不考虑当前输入 x，$m\xrightarrow{完全编码}h$ 的结果是一样。

## LSTM Long Short-Term Memory Network

!!! p "motivation"
    To solve short-term memory of RNN, LSTM can retain "important information" in longer sequence data, ignoring less important information.
    LSTMs were designed to combat vanishing gradients through a gating mechanism.

![](./pics/LSTM_1.png){width=70%}

<div class="grid" markdown>
<figure markdown="span">![](./pics/RNN_3.png)</figure>
<figure markdown="span">![](./pics/LSTM_2.png)</figure>
</div>
<p>All recurrent neural networks have chain repeating modules of neural networks. <br><mark>standard RNN</mark>: repeating module has a very simple structure, such as only a single tanh layer.<br><mark>LSTM</mark>: Not a single neural network layer, but four, and interacting in a very special way.</p>

**pre-knowledge：**

- `tanh`
  tanh activation 用於幫助調節流經網絡的值。 tanh 函數將值壓縮為始終在 -1 和 1 之間。
- `Sigmoid` $\sigma$

<div class="grid" style="grid-template-columns: repeat(3, 1fr) !important;" markdown>
<figure markdown="span" style="grid-column-start: 1; grid-column-end: 3;">![](./pics/LSTM_3.webp){width=500px}</figure>
<p style="grid-column-start: 3; grid-column-end: 4;">圆形：Neuial Network layer，一层神经网络，也就是$w^Tx*b$的操作。区别在于使用的激活函数不同<br>这里存在 sigmoid（$\sigma(w^Tx*b)$） & tanh（$\text{tanh}(w^Tx*b)$） 两种激活函数<br>方块：Matrix operation 矩阵操作，并且是 <mark>pointwise</mark> 逐元素操作<br> verctor concatenation: 矩阵拼接，变成 $(H_1+H_2)*W$ </p>
</div>

!!! p "hidden state $h_t$ & cell state $c_t$"
    相比于原始的 RNN 的 hidden state， LSTM 增加了一个细胞状态 cell state。 尽管 LSTM 中的 cell state & hidden output 都包含有关 LSTM 模型的信息，但它们的角色不同<br>
    ==hidden state== 可以被看作是**当前时刻**的 LSTM 的“理解”或“编码”信息，可以被传递到下一层的 LSTM 或者用于预测任务.<br>
    ==cell state== 是用于存储**先前的信息**和计算新的信息，一直在上面传递, internal memory

!!! p "为什么 LSTM 能携带 long-term memory？又是如何只记住重点的 memory？"
    能携带 long-term memory 因为多了一个 cell state 細胞狀態有點像傳送帶。 它直接沿著整個鏈條執行，只有一些輕微的線性相互作用。 資訊很容易不變地沿著它流動，携带整个文本的信息
    如何记住重点，则是与 ==门 gate== 息息相关。
    - 如何 忘记不重要的 & 记住重要的。
        $f_t=\sigma(\cdot)\in[0,1]$, 任何值✖️0 都是0，任何值✖️1都是它本身，所以当信息被乘以0，那么就会被忘记，如果乘以1，就会记住。$f_t$ 的数值其实就是遗忘程度。

<div class="grid" style="grid-template-columns: repeat(5, 1fr) !important;" markdown>
<figure markdown="span" style="grid-column-start: 1; grid-column-end: 4;">![](./pics/LSTM_4.webp){width=80%}<p>at time t</p></figure>
<p style="grid-column-start: 4; grid-column-end: 6;">Input:<br>-- $C_{t-1}$ cell state at t-1<br>-- $h_{t-1}$ hidden state at t-1<br>-- $x_t$ 输入的向量 at t <br>Output:<br>-- $C_{t}$<br>-- $h_{t}$<br>细胞状态 $c_{t-1}$ 一直在上面的线传递，$h_t & x_{t}$ 会对 $c$ 进行修改，输出 $c_t$ <br>$c_t$ 会参与 $h_t$ 的计算。<br> 其中的计算过程透过 <mark>门 gate</mark> 来实现。</p>4
</div>

!!! p "size of vector"
    dim(c) = dim(h)<br> shape of cell state = shape of hidden state
    > 以 遗忘门 举例：
    > $f_t^{d1\times d2}:=\sigma(W_f^{d1\times(d1+d3)}[h_{t-1}, x_t]^{(d1+d3)\times d2}+b_f)$
    > $c_{t-1}^{d1\times d2}\underline{pointwise multiplfy}f_t^{d1\times d2}$
    ![](./pics/LSTM_5.webp)

==forget gate==  决定：用当前的判断 $f$：要记得多少过去的信息 $c_{t-1}$ <br>
==input gate== 决定：用当前的判断 $i$：要加入多少当前的信息 $\tilde{c}_{t}$ <br>
==output gate== 决定：用迄今为止的判断 $o$：要向外面或者未来暴露多少信息 $c_t$ 。defines how much of the internal state you want to expose to the external network (higher layers and the next time step).<br>

### forget gate 遗忘门

当前的信息 $[h_{t-1}, x_t]$  决定 过去的信息 $c_{t-1}$ 要忘记多少

$$f_t=\sigma(W_f[h_{t-1}, x_t]+b_f)$$

![](./pics/LSTM_6.gif)

### input gate 输入门

将当前的信息 $[h_{t-1}, x_t]$ 更新到过去的信息 $c$ 里：不仅要处理要流入的值，还要决定哪些值是重要的，所以 $[h_{t-1}, x_t]$ 同时经过 Sigmoid & tanh。The sigmoid output will decide which information is important to keep from the tanh output.

$$i_t = \sigma(W_i[h_{t-1}, x_t]+b_i)\\\tilde{c}_t=\text{tanh}(W_c[h_{t-1}, x_t]+b_c)$$

![](./pics/LSTM_7.gif)

然后进行 cell state 的 update：昨日的信息 $ f_t * c_{t-1}$ 有需要遗忘的，今天的信息 $i_t * \tilde{c}_t $ 也同样有需要遗忘的

$$c_t=f_t*c_{t-1}+i_t* \tilde{c}_t$$

![](./pics/LSTM_8.gif)

### output gate 输出门

cell state $c_t$ 已更新，要过一遍 tanh 传递给下一轮的 hidden state & output for prediction，同时 当前信息 $[h_{t-1}, x_t]$ 要过 sigmoid 决定新的 $c_t$ 里有哪些是需要遗忘的。

$$o_t=\sigma(W_o[h_{t-1}, x_t]+b_o)\\h_t=o_t*\text{tanh}(c_t)$$

![](./pics/LSTM_9.gif)

![](./pics/LSTM_10.png)

t 时刻的 hidden state $h_t$ 既作为 hidden state 继续向前流动，又作为 t时刻的输出，来进行解码和完成任务。

## GNU Gated Recurrent Unit-GRU

a variant of LSTM. He retains the characteristics of LSTM to focus and forget unimportant information, and it will not be lost during long-term propagation.

GRU 将 LSTM 的 forget gate & input gate 整合到一个单独的 update gate， 还把 cell state 和 hidden state 合并成一个 hidden state，还有其他的一些小 changes。

<figure markdown="span">![](./pics/GRU_1.png)<p></p> GRU 只用 hidden state & input，而且 only 2 gates: reset gate & update gate</p></figure>

!!! p "更少的 tensor operation 更快的训练速度。"
    !!! danger "但性能上谁更好，不确定，还是要真正 train 之后才知道。"

![](./pics/GRU_2.webp)

![](./pics/GRU_3.png)

==reset gate== determines how to combine the new input with the previous memory<br>
==update gate== defines how much of the previous memory to keep around.

简单来说，把 reset 的参数都变成 1， update 的参数 都变成0，就是 standard RNN。

### Reset Gate

决定忘记哪些过去信息

### Update Gate

把 LSTM 的 forget gate & input gate 融了进来。<br>
what information to throw away and what new information to add.

## Ref

- [如何理解RNN？（理论篇）]
- [Long short-term memory network-Long short-term memory | LSTM]
- [Illustrated Guide to LSTM’s and GRU’s: A step by step explanation]
- [大名鼎鼎的LSTM详解]
- [图解LSTM实现cell state 和hidden state和output]
- [Understanding LSTM Networks]
- [Recurrent Neural Network Tutorial, Part 4 – Implementing a GRU and LSTM RNN with Python and Theano]

[如何理解RNN？（理论篇）]:https://easyai.tech/blog/rnn-understand/
[Long short-term memory network-Long short-term memory | LSTM]:https://www.easyai.tech/en/ai-definition/lstm/
[Illustrated Guide to LSTM’s and GRU’s: A step by step explanation]:https://towardsdatascience.com/illustrated-guide-to-lstms-and-gru-s-a-step-by-step-explanation-44e9eb85bf21
[大名鼎鼎的LSTM详解]: https://zhuanlan.zhihu.com/p/518848475
[图解LSTM实现cell state 和hidden state和output]:https://blog.csdn.net/u010087338/article/details/129805575
[Understanding LSTM Networks]:http://colah.github.io/posts/2015-08-Understanding-LSTMs/
[Recurrent Neural Network Tutorial, Part 4 – Implementing a GRU and LSTM RNN with Python and Theano]:https://dennybritz.com/posts/wildml/recurrent-neural-networks-tutorial-part-4/
