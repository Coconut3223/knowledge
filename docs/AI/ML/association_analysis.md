# Association Analysis

==Itemset==。A collection of one or more items. **k-itemset**: An itemset that contains k items.
==Support count σ==。 Frequency of occurrence of an itemset.
==Support s==。Fraction of transactions that contain an itemset.
==Frequent itemset==。An itemset whose support is greater than or equal to a “minsup” threshold.
==Confidence c==。Measures how often items in Y appear in records that contain X.

!!! p "Rules originating from the same itemset have identical support but can have different confidence."
    所以可以分开算。先算 support 后算 confidence。

==Association Rule==。An implication expression of form X to Y where X and Y are itemsets.
==Association Rule Mining Task==。Given a set of transactions T, the goal of association rule mining is to find all rules having

- support ≥ minsup threshold;
- confidence ≥ minconf threshold.

> > ![](./pics/AssociaA_2.png){width=60%}
> >
> > Compute the support and confidence of the association rule {Milk, Diaper} → {Beer}.
>
> N = 5 = the total number of transactions
> σ({Milk, Bread, Diaper}) = 2.
> **Support** s({Milk, Bread, Diaper}) = $\frac{\sigma}{N}=\frac{2}{5}$
> Association Rule = {Milk, Diaper} -> {Beer}
> **Confidence** c=$\cfrac{\sigma(MDB)}{\sigma(MD)}=\frac{2}{3}$

## approach

- **Frequent Itemset Generation**: Generate all itemsets whose <u>support ≥ minsup</u>.
Given $d$ items, there are $2^d − 1$ possible candidate itemsets.

![](./pics/AssociaA_1.png){width=65%}

- **Rule Generation**: Generate <u>high confidence</u> rules from each frequent itemset.

==Brute-force approach== 暴力解。列出并求出全部。Computationally prohibitive!
Each frequent itemset of size $n$ leads to $2^n−2$ association rules X → Y. 每个item都有成为X和Y两种可能，然后减掉X或Y为空的两种情况。

==Apriori principle==

- {A} Non-frequenct, $\implies$ {AB}, {AC} 更严苛的要求一定是 Non-frequent.【itemset】【support】

![](./pics/AssociaA_4.png){width=70%}

- If a rule $\{X\} → \{Y−X\}$ does not satisfy the confidence threshold, then any rule $\{X′\} →\{Y−X′\}$ where $\{X′\}\sub\{X\}$. must not satisfy the confidence threshold as well.【rule】【confidence】

==Frequent Pattern (FP)-growth algorithm==
Using the data structure **FP-tree** to extract frequent itemsets directly. An FP-tree is a compressed representation of the input. 将相同点连接，逆向找寻

> > ![](./pics/AssociaA_3.png){width=80%}
>
> search A: A=7
> search AB: 找B再看有没有A =5
> search AE：先找E再看看有没有A=1+1=2

## Da

|  | Association Rule |
| --- | --- |
| Antecedent | 前因 |
| Consequent |  |
| proximity | 近距离 |
| Itemset Lattice |  |
|  |  |

[comp9318 Association Rule Mining](https://zhuanlan.zhihu.com/p/65155693)

## Association Rule 关联规则

**An association rule is an implication of the form 𝐴 ⇒ 𝐵, where 𝐴 is the Antecedent, 𝐵 is the Consequent.**

商品放在一起可以促销，放在两端可以诱惑人们沿途购买

## Support-Confidence Framework

💡 support(itemset) 支持度 AB有关
confidence(associate rule)置信度 A推B 而不是B推A

`min_sup` : a minimum support threshold $\implies$ whether a frequent itemset $L_k$

### How to develop

1. 设定一个minimum support threshold，找到 frequent itemset $L_k$
2. Generate Strong Association Rules from the Frequent Itemsets

- Example

    support_count({I1,I2})$=\#T(I1\cup I2)=4$

    (T100，T200，T400，T800

    support({I1,I2})=$\frac{\text{support\_count}(\{ I1,I2\})}{\# T}=\frac{4}{9}$
    $\#T=9$
    Given min_sup$=\frac{2}{9}$, support({I1,I2})>$\frac{2}{9}\implies$ {I1,I2} is a frequent itemset
    confidence({I1,I2}⇒{I3})$=\frac{\text{support}(\{I1,I2,I3\})}{\text{support}(\{I1,I2\})}=\frac{2/9}{4/9}=\frac{1}{2}$

