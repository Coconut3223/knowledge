# Keyword Extraction Algorithm

## Algorithm

### TF-IDF

## Evaluation

!!! p "是在精确匹配的前提下"

### unordered results

|||
|--|--|
|Precision|$P=\cfrac{TP}{TP+FP}$|
|Recall|$R=\cfrac{TP}{TP+FN}$|
|F1-measure| $F1=\cfrac{2\times P\times R}{P+R}$|

### ordered results

#### MRR

==Mean Reciprocal Rank==. 【**第一個**正確答案多快(多早)出現？】$MRR=\cfrac{1}{|D|}\sum\limits_{d\in D}\cfrac{1}{\text{rank}_d}$

对每一个 doc 计算  $rank_d$：(应该是可以选 top3，top5)

- 对选定 ground truth keyword 计算 他在 prediction sequence 里首次出现的位置编号， 如果不存在，编号$\frac{1}{rank_d}=0$
- 对于一些都能踩中的结果来说:如果在候选词序列中，关键词的排名越靠前，该序列的MRR值越低，证明该方法更为有效。

#### MAP

==Mean Average Precision==【**整組**答案正確結果要優先出現】

> > Suppose we have a set of 5 queries Q1, Q2, Q3, Q4, and Q5, and a ranked list of 10 search results for each query. The relevance of each search result is binary, i.e., 1 if it is relevant to the query and 0 otherwise. Here is the relevance matrix for the search results:
> >
> > | Query | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 |
> > | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> >| Q1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |
> >| Q2 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
> >| Q3 | 1 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
> >| Q4 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 |
> >| Q5 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 0 |
>
> To calculate MAP, we first need to calculate the ==Average Precision (AP)== for each query. AP is calculated by taking the precision at each relevant rank position and averaging them over all relevant positions. <u>Here is how to calculate AP For Q1</u>: Relevant results: R**1, R3, R5, R9, R10**
Precision at rank 1: 1/1 = 1.0; ... at rank 2: 1/2 = 0.5; ... rank 3: 2/3 = 0.67;
... at rank 4: 2/4 = 0.5; ... at rank 5: 3/5 = 0.6
$AP_1:=AP(Q1)= (1.0 + 0.5 + 0.67 + 0.5 + 0.6) / 5 = 0.654$
<u>For Q2</u> Relevant results: R**2, R4, R6, R8, R10**
Precision at rank 1: 0/1 = 0; ... at rank 2: 1/2 = 0.5; ... rank 3: 1/3 = 0.33;
... at rank 4: 2/4 = 0.5; ... at rank 5: 2/5 = 0.4
$AP_2:=AP(Q2)= (0 + 0.5 + 0.33 + 0.5 + 0.4) / 5 = 0.3$
$\text{MAP} = \cfrac{\sum\limits^n AP_i}{n}$, where n is the number of queries.
In this example, suppose we calculate the following APs for each query:
$AP_1 = 0.654, AP_2 = 0.6, AP_3 = 0.733, AP_4 = 0.583, AP_5 = 0.55$
$MAP = (0.654 + 0.6 + 0.733 + 0.583 + 0.55) / 5 = 0.624$

#### normalized Discounted Cumulative Gain

$DCG = \sum\limits_{i=1}^p\cfrac{rel_i}{log_2(i+1)}\\IDCG= DCG\text{ under ideal situation}\\nDCG= \cfrac{DCG}{IDCG}$

对 p 个 keyword 设 rel (related score)，根据每一个关键词 的 rel 和 位置 i (index) 计算 $\frac{rel_i}{log_2(i+1)}$，IDCG则是最理想情况的DCG，按 rel 从大到小排序

## 模糊匹配的方法

具体来说，可以从词形相似度与语义相似度两个方面对关键词间的相似度进行计算，从而更有效地评估提取的效果。前者一般采用编辑距离算法［86］进行计算，后者的计算方式因研究而异，如Dagan等利用概率模型计算单词间的相似度［87］。考虑到单一的相似度方法存在局限，文献［88］在计算时综合考虑了关键词间语义相似度与词形相似度
