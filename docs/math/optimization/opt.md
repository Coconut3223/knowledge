# Optimization 最优化

==Optimization== finds the <u>“best”</u> possible solutions from a set of feasible points.

## Problem

An optimization problem takes the form of **minimizing (or maximizing) an objective function subject to constraints**.

$$ \min f(x)\text{ s.t.} x\in\Omega $$
$x$, decision variables  决策变量
$f$, the objective function  目标函数
$\Omega$, the constraint set / feasible set / feasible region   可行空间

|凸优化|无约束凸优化 |约束凸优化问题|
|--|--|--|
|目标函数| 凸函数||
|定义域|凸集||
|不等式约束|❌|凸函数|
|等式约束函数|^|仿射函数|

### $f$ objective function

||$f(x) = $||
|--|--|--|
|Linear|$w^T x$| $w\in\R^d$ 线性变换|
|Affine,仿射函数|$w^T x +\red{b}$|$ w\in R^n, b\in R$最高次数为1的多项式函数|
|Quadratic 二次函数|$\red{\frac{1}{2}x^TGx}+w^Tx+b$|$G\in S^{n\times n},w\in R^n, b\in R$<br> $\nabla f(x)=Gx+w$|

!!! p "$G\in S^{n\times n}$ in Quadratic func 一定会是对称"
    $x^TGx\in\R\implies (x^TGx)^T=x^TG^Tx=x^TGx\implies G=G^T$

### Constraints

|constraints||f||
|--|--|--|--|
|Unconstrained|| $\Omega\in\R^n$|
|Equality |sphere 球面|$x_1^2+\dots+x_n^2=1$|
|^|hyperplane 超平面|$x_1+\dots+x_n=1$
|^|paraboloid 抛物面|$x\in R^3:x_1^2+x_2^2=x_3$
|Inequality|ball 球体|$x_1^2+\dots+x_n^2≤1$
|^|half-space 半空间|$x_1+\dots+x_n≤0$
||$x\in R^3:x_1^2+x_2^2≤x_3$
|Box|$\ell≤x≤u$, $\ell\in R^n$, $u \in R^n$$\ell_i≤x_i≤u_i,\forall i$ 按分量逐位(*component-wise*)

### Minimizer

!!! p "是否存在最优值"
    函数 $f$ 的最值不一定存在，但是其<u>下(上)确界</u>$\inf f(\sup f)$ 总是存在的。
    $$f^*=\begin{cases}\min(\max) f &\text{存在}\\\inf(\sup)f&\text{不存在}  \end{cases}$$

    **Existence of Infimum**: 
    $$\quad\Omega\subset\R^n\text{, a nonempty compact set},f\text{ be continuous on }\Omega \\
    \implies f\text{ can achieve its infimum values over }\Omega\\
    \text{i.e. } \exist x^*\in\Omega\text{ s.t. }f(x^*)=\inf\{f(x):x\in\Omega\}$$
    
    !!! p "In general, finding global minimizers for f is NP-hard. In order to set a modest goal, we look at more properties of local minimizers."

- $x^*$ is a ==global minimizer，全局最小== of $f\impliedby f(x)≥f(x^*), \forall x\in\R^n$
- $x^*$ is a ==local minimizer，局部最小== of $f \impliedby\exist  \epsilon>0,f(x)≥f(x^*), \forall x \in\{\Vert x-x^*\Vert_2<\epsilon\}$
    - $x^*$邻域，邻域就是包含它的一个无穷小量的球，**在邻域**的范围内
    - 如果严格不取等，那么就称它为**严格局部最小值**

#### 解的最优性条件

!!! danger "大多数情况下，我们寻求的是局部最优."
    给出一个一阶可导且连续的函数 $f\in C^1(R^n)$:
    1. 通过$\nabla f(x*)=0$找到驻点$X=x^*$
    2. 通过 $\nabla^2 f(x^*)$ 去验证 $X=x^*$ 是否local minimizer（Hessian矩阵好算的情况下

    | 唯一解 | 无穷解或无解 | 方程解 |
    | --- | --- | --- |
    | 不满秩 | 不满秩 | 秩 |
    | $\vert A \vert≠0$ | $\vert A \vert=0$ | $\vert A \vert$ 行列式 |
    | invertible 可逆 | uninvertible 不可逆 | 普通 |
    | insingular 非奇异  | singular 奇异  | 方阵 |
    | >0 | ≥0 | 特征值 eigenvalue $\in$ 实对称矩阵 |
    | positive definite 正定的 | positive semi-definite 半正定的 |  ^|

假设$f(x)$具有二阶连续偏导数，若第k次迭代值为$x^k$，则可将$f(x)$$在x^k$进行二阶泰勒展开：
$f(x)=f(x^{k})+ \nabla f(x^k)^T\cdot (x-x^k)+\frac{1}{2}(x-x^k)^T\cdot\nabla^2f(x^k)\cdot(x-x^k)$
$$\red{\nabla f(x^*)=0\implies x^* \text{是}f(x)的极值点(驻点)\\\xRightarrow{\nabla^2f(x^*)\succ0}x^* \text{是}f(x)的极小值点}$$

下面开始证明：

##### 1st-order necessary conditions 一阶必要条件

$$f\in C^1(\R^n), x^*\text{ is a local minimizer of } f\implies \nabla f(x^*) = 0$$
若$f(x)$ 在$\R^n$上有**一阶连续偏导数**，且$x^*$为局部最优解，则必有$\nabla f(x^*)=0$

!!! p "一阶导等于0，证明的是该点是驻点，==stationary point==，是极值点，但可能是极小值，也有可能是极大值"

##### 2nd-order necessary conditions 二阶必要条件

$$f\in C^2(\R^n),x^*\text{ is a local minimizer of } f\implies \nabla^2 f(x^*) \bold{\red{\succeq}} 0$$

若$f(x)$ 在$\R^n$上有**二阶连续偏导数**，且$x^*$为局部最优解，则必有$\nabla^2 f(x^*)\bold{\red{\succeq}} 0$ 即  $\nabla^2 f(x^*)$ 是<u>半正定矩阵，positive semifinite matrix</u>.

##### 2nd-order sufficient conditions 二阶充分条件

$$\begin{cases}f\in C^2(\R^n)\\
x^*\text{ is a stationary point of } f\\
\nabla^2 f(x^*) \red{\bold{\succ 0}}
\end{cases}\implies
x^*\text{ is a local minimizer of } f$$

若$f(x)$ 在$\R^n$上有**二阶连续偏导数**，且$\space x^*$ 已经是驻点且$\space \nabla^2 f(x^*)\bold{\red{\succ}} 0$，则必有$x^*$是局部最优

!!! danger "判断局部最优时，二阶导一定要是<u>**正定矩阵**</u> $\nabla^2f(x^*)\succ0$ <br> $\begin{cases}\nabla f(x^*)=0\\\nabla^2f(x^*)\succeq0 \end{cases}\nRightarrow\text{local minimizer}$"
    > (L2.exp2 in AMA505) Consider $f(x)=(x_2^2-x_2^4)(x_2^2-\cfrac{x_1^4}{4})$ at the stationary point $(0, 0)$ . Then for any $h \in\R^2|\{0\}$, there $\exist t_0 > 0$ such that $f(th) > 0. \forall t\in (0, t_0)$. However, $(0, 0)$ is not a local minimizer of $f$! Note, however, that $\nabla^2f((0,0))=0\succeq0$【limitation】

!!! p "是否local minimizer or local maximizer"
    1. $\nabla f(x)=\begin{bmatrix} \frac{\partial f}{\partial x_1} \\\frac{\partial f}{\partial x_2}\end{bmatrix} \xlongequal{SET}0 \implies x^* \text{ is stationarty point}$
    2. compute $\nabla^2f(x)= \begin{bmatrix} \frac{\partial^2f}{\partial x_1\partial x_1} &\frac{\partial^2f}{\partial x_1\partial x_2} \\\frac{\partial^2f}{\partial x_2\partial x_1}&\frac{\partial^2f}{\partial x_2\partial x_2}\end{bmatrix},$
    3. Let $\begin{vmatrix}\nabla^2f(x^*-\lambda I)\end{vmatrix}=0,\nabla^2f(x^*)\text{ has eigenvalues }\lambda_1,\lambda_2$
    4. $\lambda_1\lambda_2 \begin{cases}\text{ both >}&\nabla^2f(x^*)\succ0&x^*\text{ is local minimizer}\\\text{ both <}&\nabla^2f(x^*)\prec 0&x^*\text{ is local maximizer}\\\text{ > and <}&\nabla^2f(x^*)\text{ is indefinite }&x^*\text{not local mini../maxi…}&\end{cases}$

    > > (Ex. 3 in L1 in AMA505) Compute the gradient and Hessian of the Rosenbrock func:$f(x)=100(x_2-x_1^2)^2+(1-x_1)^2$ Show that $x^* = [1,1]^T$ is its **only minimize**r and the Hessian is positive definite at $x^*$.
    >
    > $\nabla f(x)=\begin{bmatrix}-400(x_2-x_1^2)x_1-2(1-x_1)\\200(x_2-x_1^2)\end{bmatrix}, \nabla f(\begin{bmatrix}1\\1\end{bmatrix})=0\implies$ stationary point
    $\nabla^2f(x)=\begin{bmatrix}-400x_2+1200x_1^2+2&-400x_1\\-400x_1&200\end{bmatrix},\nabla^2f(\begin{bmatrix}1\\1\end{bmatrix})=\begin{bmatrix}802&-400\\-400&200\end{bmatrix}$
    $\begin{cases}\lambda_1+\lambda_2=1002\\\lambda_1*\lambda_2=\Vert\nabla^2f\Vert=400\end{cases}\implies\lambda_1\gt0,\lambda_2\gt0\implies\nabla^2f\succ0$
    obviously, $\forall x, f(x)\ge0\implies \min\limits_x(f)=0, \text{with }x_1=1$
    $\implies x_2=x_1=1\implies \begin{bmatrix}1//1\end{bmatrix}$ is the only one minimizer.

    > > (Ex. 4 in L1 in AMA505) Find all the stationary points and determine their nature, if possible.$ f(x)=x_1^4 +x_2^4-4x_1x_2 +2$
    >
    > $\nabla f(x)=\begin{bmatrix}4x_1^3-4x_2\\4x_2^3-4x_1\end{bmatrix}\xlongequal{SET}0\implies x_1=x_2=0,1,-1. \qquad\nabla^2f(x)=\begin{bmatrix}12x_1^2&-4\\-4&12x_2^2\end{bmatrix}$
    $\nabla^2f(\begin{bmatrix}0\\0\end{bmatrix})=\begin{bmatrix}0&-4\\-4&0\end{bmatrix}\begin{cases}\lambda_1+\lambda_2=0\\\lambda_1*\lambda_2=-16\end{cases}\implies (4, -4)\implies$ (0,0) is not local minimizer or maximizer
    $\nabla^2f(\begin{bmatrix}1\\1\end{bmatrix})=\nabla^2f(\begin{bmatrix}-1\\-1\end{bmatrix})=\begin{bmatrix}12&-4\\-4&12\end{bmatrix}\begin{cases}\lambda_1+\lambda_2\gt0\\\lambda_1*\lambda_2\gt0\end{cases}\implies \lambda\gt0\implies$(1,1),(-1, -1) is local minimizer

    > > (T1 in Hw1 in AMA505) Find all the stationary points and determine their nature based on their Hessian, if possible. 
    > > $f(x)=\frac{1}{2}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}^T\begin{bmatrix}3&1&0\\1&4&0\\0&0&5\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}-4x_1-5x_2-5x_3^3+7$
    > 
    > $A:=\begin{bmatrix}3&1&0\\1&4&0\\0&0&5\end{bmatrix},b:=\begin{bmatrix}4\\5\\0\end{bmatrix}\implies f(x)=\frac{1}{2}x^TAx-b^Tx-5x^3+7$
    $\nabla f(x)=Ax-b-\cfrac{\partial 5x^3}{\partial x}=\begin{bmatrix}3x_1+x_2-4\\x_1+4x_2-5\\5x_3-15x_3^2\end{bmatrix}\xlongequal{SET}0\implies x_1=x_2=1, x_3 = 0,\frac{1}{3}$
    $\begin{bmatrix}1&1&0\end{bmatrix}^T, \begin{bmatrix}1&1&\frac{1}{3}\end{bmatrix}^T$ are stationary points.
    $\nabla^2f(x)=A-\cfrac{\partial^25x_3^3}{(\partial x)^2}=\begin{bmatrix}3&1&0\\1&4&0\\0&0&5-30x_3\end{bmatrix}$
    $\nabla^2f((1,1,0))=\begin{bmatrix}3&1&0\\1&4&0\\0&0&5\end{bmatrix}$ 
    $\nabla^2f((1,1,\frac{1}{3}))=\begin{bmatrix}3&1&0\\1&4&0\\0&0&-5\end{bmatrix}$
    $D_1=\begin{bmatrix}3\end{bmatrix}\succ0, D_2=\begin{bmatrix}3&1\\1&4\end{bmatrix}\begin{cases}\sum\lambda\gt0\\\prod\lambda\gt\end{cases}\implies D_2\succ0$
    for $(1,1,0) \begin{cases}\sum\lambda=12\\\prod\lambda=55\end{cases}\implies\succ0\implies$ is the local minimizer.
    for $(1,1,\frac{1}{3}) \begin{cases}\sum\lambda=2\gt0\\\prod\lambda=-55\lt0\end{cases}\implies\text{indefinite}\implies$ is not the local minimizer or maximizer

[最优化学习 无约束优化问题的最优性条件]
## method

|优化法||notes|
|---|---|---|
Derivative-free<br>无导数优化| Pattern search 模式搜索
^| Grid search 网格搜索
^| NM算法, Nelder-Mead method
Derivative-based 导数优化 | Steepest descent 最速下降法
^| Newton’s method  牛顿迭代法 | if $f \in C^2$
^| Quasi-Newton method 拟牛顿法

### 迭代法

给起始点$x^0$,找到下一个点$x^1,x^2,…$一直找到目标点 $x^*$

==终止条件==
-  $\Vert\nabla f(x*)\Vert=0 \rightarrow \Vert\nabla f(x^n)\Vert<\varepsilon$
-  $\Vert x^n-x^*\Vert<\varepsilon$， x区间很小，小于精度
-  $\Big\vert\cfrac{f(x^{n+1})-f(x^n)}{???}\Big\vert<\varepsilon$

**收敛性**: 考虑算法产生的点列是否收敛到优化问题的解
- ==全局收敛==, $\forall x^0,x^k\rightarrow x^*$
- ==局部收敛==, $\forall x^0\in N(x^*),x^k\rightarrow x^*$邻域内收敛

收敛速度
| $\Vert x^k-x^*\Vert\rightarrow 0$ |  |
| --- | --- |
| 线性 | $\Vert x^{k+1}-x^*\Vert≤r\Vert x^k-x^*\Vert,0<r<1$ |
| 超线性 | $\Vert x^{k+1}-x^*\Vert=\circ\Vert x^k-x^*\Vert \iff \cfrac{\Vert x^{k+1}-x^*\Vert}{\Vert x^k-x^*\Vert}=0$ |
| 二次 | $\Vert x^{k+1}-x^*\Vert≤L\Vert x^k-x^*\Vert^2$ |

## 分类

都是对函数 *f* (*x*) 在局部进行近似，但处理近似问题的方式不同

### line search 线搜索

$\text{ given a point }x^k, \text{ ①  find a descent direction }d^k,\text{ then ② find a stepsize }\alpha^k>0,\text{ then }\\\qquad\qquad\qquad\qquad\qquad\qquad
x^{k+1}=x^{k}+\alpha^kd^k$

### trust religion method 信赖域

x^k一个球去找区间

[最优化学习 无约束优化问题的最优性条件]: https://blog.csdn.net/weixin_45508265/article/details/117376386
