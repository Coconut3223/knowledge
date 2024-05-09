# Linear Algebra

## Eigen Decoposition 特征值分解

==Eigen Decoposition==. $\forall A\in\R^n，\exist\lambda, x\text{ s.t. }Ax=\lambda x$

- $x:= $ 特征向量 eigenvector
- $\lambda:=$ 特征值 eigenvalue
可以是复数，但 $A^T=A\implies \forall\lambda\in\R$
- $A$ 必须是方阵

!!! warning "接下来研究的 covariance matrix $\in S^n\implies \forall\lambda\in\R$
"
由 eigen decomposition 推 ==对角化 diagonalization==. $A=U\Lambda U^T$
$x_i=$ eigenvectors of $A$, $U=\begin{bmatrix}x_1&\dots&x_n\end{bmatrix}\in\R^n$
$U\Lambda U^T=\begin{bmatrix}x_1&\dots&x_n\end{bmatrix}\begin{bmatrix}\lambda_1\\&\ddots\\&&\lambda_n\end{bmatrix}\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix}=\begin{bmatrix}\lambda_1x_1x_1^T\\&\ddots\\&&\lambda_nx_nx_n^T\end{bmatrix}$

## Singular value decomposition SVD

!!! danger "SVD 正交分解 $\neq$ Eigen Decoposition 特征值分解"
    虽然对半正定矩阵来说，SVD is a special eigen decomposition.

==SVD== $\forall A\in\R^{m\times n}, A\xlongequal{\text{can be factored into}} U\Sigma V^T=\text{(orthogonal)(Diagonal)(orthogonal)}$

- $U\in \R^{m\times m}$. **Orthogooal** $U^TU=I$
The columns of $U$ are eigenvectors of $AA^T\in\R{m\times m}$
- $V\in\R^{n\times n}$ **Orthogooal** $V^TV=I$
The columns of $V$ are eigenvectors of $A^TA\in\R^{n\times n}$.
- $\Sigma\in\R^{m\times n}$ **Diagonal**
The $\red{r}$ singular values on the diagonal of $\Sigma$ are **the square roots** of the **nonzero eigenvalues** of both $AA^T \& A^TA$

**Proof:**
Suppose $m>n, \Sigma=\begin{bmatrix}\theta_1\\&\ddots\\&&\theta_n\\&&\end{bmatrix}\in\R^{m\times n}$

$\Sigma^T\Sigma=\begin{bmatrix}\theta_1\\&\ddots\\&&\theta_n&\end{bmatrix}\begin{bmatrix}\theta_1\\&\ddots\\&&\theta_n\\&\end{bmatrix}=\begin{bmatrix}\theta_1^2\\&\ddots\\&&\theta_n^2\end{bmatrix}\in S^n$
$\Sigma\Sigma^T=\begin{bmatrix}\theta_1\\&\ddots\\&&\theta_n\\&\end{bmatrix}\begin{bmatrix}\theta_1\\&\ddots\\&&\theta_n&\end{bmatrix}=\begin{bmatrix}\theta_1^2\\&\ddots\\&&\theta_n^2&\\&\end{bmatrix}\in S^m$

$$\begin{align*}
A^TA&=V\Sigma^TU^TU\Sigma V^T\xlongequal{U^TU=I}V\Sigma^T\Sigma V^T\in S^n\\
AA^T&=U\Sigma V^TV\Sigma^TU^T\xlongequal{V^TV=I}U\Sigma\Sigma^TU^T\in S^m
\end{align*}$$

因为 **对称方阵都能进行特征分解** $A=U\Lambda U^T$
$x_i=$ eigenvectors of $A$, $U=\begin{bmatrix}x_1&\dots&x_n\end{bmatrix}\in\R^{n\times n}$
$U\Lambda U^T=\begin{bmatrix}x_1&\dots&x_n\end{bmatrix}\begin{bmatrix}\lambda_1\\&\ddots\\&&\lambda_n\end{bmatrix}\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix}=\lambda_1x_1x_1^T+\dots+\lambda_nx_nx_n^T$

$V\Sigma^T\Sigma V^T\xlongequal{SVD}A^TA=S_1\xlongequal{\text{eigen decomp}}U_1\Lambda_1U_1^T\begin{cases}U_1=V\\\Lambda_1=\Sigma^T\Sigma\end{cases}
\\
U\Sigma\Sigma^TU^T\xlongequal{SVD}AA^T=S_2\xlongequal{\text{eigen decomp}}U_2\Lambda_2U_2^T\begin{cases}U_2=U\\\Lambda_2=\Sigma\Sigma^T\end{cases}$
$\begin{bmatrix}\lambda_1\\&\ddots\\&&\lambda_n\end{bmatrix}_1=\Lambda_1=\Sigma^T\Sigma=\begin{bmatrix}\theta_1^2\\&\ddots\\&&\theta_n^2\end{bmatrix}$
$\begin{bmatrix}\lambda_1\\&\ddots\\&&\lambda_m\end{bmatrix}_2=\Lambda_2=\Sigma\Sigma^T=\begin{bmatrix}\theta_1^2\\&\ddots\\&&\theta_n^2&\\&\end{bmatrix}$
$\implies$
- The columns of $U$ are eigenvectors of $AA^T\in\R^{m\times m}$
- The columns of $V$ are eigenvectors of $A^TA\in\R^{n\times n}$.
- $\lambda_i=\theta_i^2\implies$ The $\red{r}$ singular values on the diagonal of $\Sigma$ are **the square roots** of the **nonzero eigenvalues** of both $AA^T \& A^TA$
