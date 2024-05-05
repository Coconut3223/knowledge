# Machine Translation MT 机器翻译

==Neural Machine Translation NMT==。
==Statistical Machine Translation SMT==。rule-based & statistical techniques

## NMT

<figure markdown="span">
  ![](./pics/NMT_1.png)
  <p class=notes><b>Figure 1</b>: Schematic view of neural machine translation。<br>The red source words are first mapped to word vectors and then fed into a recurrent neural network (RNN). Upon seeing the ⟨eos⟩ symbol, the final time step initializes a target blue RNN. <br> At each target time step, attention is applied over the source RNN and combined with the current hidden state to produce a prediction of the next word. This prediction is then fed back into the target RNN.</p>
</figure>

NMT takes a **conditional language modeling**
view of translation by modeling the probability of a target sentence $w_{1:T}$ given a source sentence $x_{1:S}$ as $$p(w_{1:T}|x) = \prod_{t=1}^Tp(w_t|w_{1:t−1}, x; θ)$$
This distribution is estimated using an attention-based en-decoder architecture (Bahdanau et al., 2014).
A source encoder recurrent neural network (RNN) maps each source word to a word vector, and processes these to a sequence of hidden vectors $h_1,...,h_S$.
The target decoder combines an RNN hidden representation of previously generated words $(w_1,...w_{t−1})$ with source hidden vectors to predict scores for each possible next word.
A softmax layer is then used to produce a next-word distribution $p(w_t|w_{1:t−1}, x; θ)$.
The source hidden vectors influence the distribution through an attention pooling layer that weights each source word relative to its expected contribution to the target prediction.
The complete model is trained end-to-end to maximize the likelihood of the training data. An unfolded network diagram is shown in Figure 1.

**improve the effectiveness of the base model:**

- **a gated RNN such as an LSTM** (Hochreiter and Schmidhuber, 1997) or **GRU** (Chung et al., 2014) which help the model <u>learn long-distance features within a text</u>.
- **relatively large, stacked RNNs**, which consist of several vertical layers (2-16) of RNNs at each time step (Sutskever et al., 2014).
- <u>Input feeding</u>, where **the previous attention vector + predicted word** is fed back into the input.(Luong et al., 2015).
- Test-time decoding is done through beam search where multiple hypothesis target predictions are considered at each time step. Implementing these correctly can be difficult, which motivates their inclusion in an NMT framework.
