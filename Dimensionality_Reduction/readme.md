# Dimensionality Reduction

A technique that reduces the number of features in a dataset while retaining the most important properties of the original data. The goal is to simplify complex data so it's easier to process and analyze. 

a) Image data set Colab Link: https://colab.research.google.com/drive/1QVhoKYY1GVzK1DQbQOgBK03ujOdXvHEg?usp=sharing 

b) Tabular data set Colab Link: https://colab.research.google.com/drive/1M_hEGgpaVZ7qM-QhfGzFDnnim5UbZsrh?usp=sharing 

Youtube Link: https://youtu.be/uZpte2rbBnk 


### Comparision between Dimensionality Reduction Techniques and Commentary on Results:

## Locally Linear Embedding (LLE) 

**Observation**: LLE captures local relationships well, making it effective for datasets with non-linear structures. For instance, clusters in the Wine dataset may be preserved, but global relationships between clusters might be distorted. 

**Strengths**: Excellent for non-linear manifolds; focuses on preserving neighborhood structure.

**Weaknesses**: Sensitive to noise and outliers; computationally expensive for large datasets.


## t-SNE 

**Observation**: t-SNE produces visually appealing 2D representations that clearly separate clusters (e.g., in the Digits dataset). However, it doesn’t preserve global structures well, which might make interpretations challenging. 

**Strengths**: Ideal for visualizing high-dimensional data in 2D or 3D; emphasizes cluster separation.

**Weaknesses**: Computationally expensive; results depend heavily on hyperparameters like perplexity.


## ISOMAP 

**Observation**: ISOMAP retains both local and global geometry better than LLE. For example, it may display clear cluster separations in the Breast Cancer dataset while maintaining inter-cluster distances. 

**Strengths**: Good balance between preserving global and local structures. 

**Weaknesses**: Sensitive to the number of neighbors chosen; computationally slower than t-SNE or UMAP.


## UMAP 

**Observation**: UMAP balances clarity and speed. For example, it effectively separates clusters in the Digits dataset, similar to t-SNE, but is much faster. It also handles large datasets well. 

**Strengths**: Fast, scalable, and versatile; preserves both local and global structure. 

**Weaknesses**: Requires tuning parameters for best results (e.g., n_neighbors and min_dist).


## Multidimensional Scaling (MDS) 

**Observation**: MDS emphasizes preserving pairwise distances in the Wine dataset. It provides a reasonable representation but doesn’t perform well for complex non-linear manifolds. 

**Strengths**: Simple to use; preserves pairwise distances. 

**Weaknesses**: Computationally expensive; less effective for non-linear data.


## Randomized PCA 

**Observation**: Randomized PCA produces similar results to standard PCA but is computationally faster for large datasets like Breast Cancer. It preserves variance effectively but assumes linearity in data. 

**Strengths**: Fast and scalable for large datasets; preserves variance. 

**Weaknesses**: Limited to linear transformations.


## Kernel PCA 

**Observation**: Kernel PCA excels in capturing non-linear relationships, as seen in the Digits dataset. The choice of kernel (e.g., RBF or polynomial) significantly impacts results. 

**Strengths**: Extends PCA to non-linear data; customizable through kernel selection. 

**Weaknesses**: Computationally intensive; results are sensitive to kernel and parameter selection.


## Incremental PCA 

**Observation**: Incremental PCA works similarly to standard PCA but handles large datasets like Breast Cancer more efficiently by processing data in batches. 

**Strengths**: Efficient for large datasets; preserves variance like PCA. 

**Weaknesses**: Limited to linear transformations.


## Factor Analysis 

**Observation**: Factor Analysis provides interpretable latent variables but is not as effective for visualizing clusters in datasets like Wine. 

**Strengths**: Useful for understanding latent factors in data. 

**Weaknesses**: Assumes linearity and Gaussian distributions.


## Autoencoders 

**Observation**: Autoencoders produce embeddings that can separate clusters well in the Digits dataset. However, they require more computational resources and careful tuning of the neural network architecture.

**Strengths**: Highly flexible; captures non-linear relationships effectively. 

**Weaknesses**: Computationally intensive; requires tuning of architecture and hyperparameters. 

