# ?

### Dynamic Step Size Adjusting:

- Decrease the step size by ratio $γ\in(0,1)$  every K epochs.
- **Epoch Doubling Strategy**

    Run K epochs with step size 𝛼, then, run 2K epochs with step size 𝛼/2, ......

## Noise Reduction Methods

在机器学习中，最常用的优化算法就是SGD(随机梯度下降算法)，我们发现它在但是SGD由于每次迭代方向都是随机选择的，所以产生了下降方向的噪音的方差。正是由于这个方差的存在，所以导致了SGD在每次迭代（使用固定步长α）时，最终是收敛不到最优值的，最优间隔最终趋于一个和方差有关的定值。为了克服这一点，我们采取一种办法，是想要让方差呈递减趋势下降，那么最终算法的将会以线性速度收敛于最优值。

💡 To reduce the $\colorbox{aqua}{\text{B}}\text{ in } \colorbox{aqua}{\text{(1)}}$

### **Dynamic Sampling**

### **Gradient Aggregation**

💡 Correct the bias of the stochastic estimation of gradients using historical gradients estimates. 使用历史梯度估计来纠正梯度随机估计的偏差。

**Stochastic Variance Reduced Gradient Method, SVRG，** 随机方差缩减梯度下降法

主要技巧是缓存一个梯度向量，通过缓存向量与最新梯度的距离能给出梯度方差的上界．

Correct the bias of the stochastic estimation of gradients **using full batch gradient every m iterations.**

看到SVRG的计算量相比较SGD大得多

**Stochastic Average Gradient Accelerated, SAGA**

Correct the bias of the stochastic estimation of gradients **using historical stochastic gradient information.**

其后，SAGA［Defazio et al.，2014］改进了SAG算法，使用随机方差缩减梯度下降法（SVRG）的技巧将SAG中的梯度改成了无偏的估计．

### **Iteration Averaging**

- 📑 ref
Introductory Lectures on Convex Programming, Volume I: Basic course, Yu. Nesterov July 2, 1998

# Optimization Problem Setting

$$
\argmin\limits_{\theta\in\R^s}R_n(\theta):=\cfrac{1}{n}\sum\limits_{i=1}^nl(\theta;X_i,Y_i)
$$

Assumption:

1. $f\text{ is L-smooth}$ 
    
    $\colorbox{aqua}{\text{L-smooth}}\\\quad\begin{cases}f(\theta) \text{ is continuously differentialble}\iff f\in C^2(\R^n)\\\nabla f(\theta) \text{ is Lipschitz continuous}\iff \exist L>0, \Vert\nabla f(x)-\nabla f(y)\Vert\le L\Vert x-y\Vert\\\end{cases}\\\quad\implies f \text{ is L-smooth}$
    
    - proof:
        
        $\colorbox{aqua}{\text{Lemma 3.1}} \text{ Given a L-smooth function }f\\\quad \forall x,y\in\text{dom}(f),f(y)\le f(x)+\nabla f(x)^T(y-x)+\cfrac{L}{2}\Vert y-x\Vert^2$
        
        $**\implies \alpha_k:=\frac{1}{L}$ is feasible and optimal**
        
        - proof
            
            ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c93ca89b-e83a-457c-b37c-670a742cf27c/Untitled.jpeg)
            
            ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9ad40e5e-8076-42b1-9ad1-2396446b23bf/Untitled.jpeg)
