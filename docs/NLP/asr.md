# Automatic Speech Recognition ASR

Traditionally, ASR systems consist of acoustic, pronunciation and language models that are optimized independently.

## Code-switching

> 同我再 check 一下？ ==intra-sentential code-switching 句内转换==。
> 同我再检查一下。 I will arrive at Friday. ==inter-sentential code-switching 句外转换==。

**challenges for traditional ASR based system:**

- the requirement of hand-crafted components, such as a well-designed mixed phone set and the corresponding pronunciation lexicon.

End-to-end (E2E) models directly optimize the probability of output sequences given input speech observations with a single network, thus provide an elegant solution to build a ASR system. Recent work on E2E models can be categorized into three main approaches: Connectionist Temporal Classifi- cation (CTC) [6], RNN-Transducer [7, 8] and attention-based sequence-to-sequence models [9, 10]. Besides, joint CTC- attention model [11, 12] exploits the advantages from both CTC and sequence-to-sequence models within the multi-task learn- ing framework, which leads to better performance and robust- ness. E2E ASR models have made promising progress in many areas including monolingual [13, 14], multilingual [15, 16] and multi-speaker [17] speech recognition task. It’s also shown that attention-based sequence-to-sequence models are able to
