# Hierarchial Clustering:

hint : https://colab.sandbox.google.com/github/saskeli/data-analysis-with-python-summer-2019/blob/master/clustering.ipynb

# Solution:

Colab Links: https://colab.research.google.com/drive/1N41jeudkvBaZuEO9TG7vZa8TqeqbLSQV?usp=sharing 
             https://colab.research.google.com/drive/18T77Z5cupQE-7k49H7aRtw9SO-7HIEkT?usp=sharing

Yotube Link: 

### Key Learnings:

## **Hierarchial Clustering:**
Hierarchical clustering is a type of unsupervised machine learning algorithm used to group data into clusters based on similarity. Unlike K-Means, it doesn't require the number of clusters (k) to be specified upfront. Instead, it builds a tree-like structure, known as a dendrogram, to represent the data's hierarchical relationships. Hierarchical clustering creates a hierarchy of clusters that can be visualized as a tree. There are two main types:

### Agglomerative (Bottom-Up):

Starts with each data point as its own cluster. Gradually merges the closest clusters until only one cluster remains (the entire dataset).
Most commonly used.

### Divisive (Top-Down):

Starts with the entire dataset as one cluster.
Recursively splits clusters into smaller ones until each data point is its own cluster.

### Steps in Agglomerative Hierarchical Clustering:

**Calculate Pairwise Distances**: Compute the distances between all data points using a distance metric (e.g., Euclidean distance).

**Merge Closest Clusters**: Identify the two closest clusters and merge them.

**Update Distance Matrix**: Update the distance matrix to reflect the distance between the new cluster and all remaining clusters.

Repeat: Repeat steps 2 and 3 until all points are merged into a single cluster.

**Visualize with a Dendrogram**: Use the dendrogram to decide how many clusters to form by "cutting" the tree at a chosen level.




