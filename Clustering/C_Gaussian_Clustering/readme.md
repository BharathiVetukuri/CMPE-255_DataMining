# Gaussian Mixture Models Clustering:

hint : https://colab.sandbox.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.12-Gaussian-Mixtures.ipynb

# Solution:

Colab Links: https://colab.research.google.com/drive/1dP58y4aWq9i8Xkx3mjntILLvKPwrpgho?usp=sharing 
              https://colab.research.google.com/drive/1e_W6pcO57pChNkTEg83gUoFtxDgKpgYu?usp=sharing 

Yotube Link: 

### Key Learnings:

## **Gaussian Mixture Models (GMM) for Clustering:**
Gaussian Mixture Models (GMM) are a probabilistic clustering approach that assumes the data is generated from a mixture of several Gaussian distributions. Unlike K-Means, which assigns each point to the nearest cluster centroid, GMM assigns probabilities of belonging to each cluster.

### How GMM Works:

**Gaussian Distribution:**

Each cluster is modeled as a Gaussian (normal) distribution defined by:
Mean (μ): Center of the cluster.
Covariance (Σ): Shape and orientation of the cluster.

Soft Clustering:

Instead of assigning each point to a single cluster, GMM assigns probabilities for a point to belong to each cluster.
Expectation-Maximization (EM) Algorithm:

GMM uses the EM algorithm to optimize the parameters:
E-Step (Expectation): Estimate the probabilities of each data point belonging to each cluster based on current parameters.
M-Step (Maximization): Update the parameters (μ,Σ, and cluster weights) to maximize the likelihood of the data.

Gaussian Mixture Models provide a powerful way to cluster data with overlapping or non-spherical distributions. While computationally intensive, GMM offers flexibility and probabilistic insights into clustering, making it suitable for a wide range of real-world applications.





