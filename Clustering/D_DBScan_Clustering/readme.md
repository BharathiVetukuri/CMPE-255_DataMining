# DB Scan Clustering Using Pycaret Library :

Hint: https://pycaret.org/create-model/ 

https://towardsdatascience.com/clustering-made-easy-with-pycaret-656316c0b080

http://www.pycaret.org/tutorials/html/CLU101.html

# Solution:

Colab Links: https://colab.research.google.com/drive/1UR-e6rJuVO8jV40mFo1-KTn5EakJN-3w?usp=sharing 
              https://colab.research.google.com/drive/1F_keKl-VTOXjZu7JkmJrgZ_sad-K9MUQ?usp=sharing

Yotube Link: https://youtu.be/1tjB-X4JdW4 

### Key Learnings:

## **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**
DBSCAN is a clustering algorithm that groups data points based on their density and identifies outliers as noise. Unlike K-Means or Gaussian Mixture Models, DBSCAN does not require specifying the number of clusters in advance. Instead, it uses two parameters:

Epsilon (ε): Maximum distance between two points for them to be considered in the same neighborhood.
MinPts: Minimum number of points required to form a dense region (a cluster).

### How DBScan Works:

**Core Points:** A point is a core point if it has at least MinPts neighbors within a distance of ε.

**Border Points:** A point is a border point if it is not a core point but lies within the ε neighborhood of a core point.

**Noise:** Points that are neither core points nor border points are classified as noise.

**Clustering:** Clusters are formed by connecting core points and their neighbors.

DBSCAN is a powerful clustering algorithm for identifying clusters of arbitrary shapes and densities. While parameter selection can be challenging, it excels in applications with noisy or irregularly distributed data. For best results, combine it with tools like the k-distance plot and evaluation metrics such as the Silhouette Score.


### DBSCAN Clustering with PyCaret:

PyCaret is a low-code machine learning library that simplifies the process of building, training, and deploying machine learning models. It includes support for clustering algorithms like DBSCAN in its clustering module.

Using PyCaret simplifies the process of applying DBSCAN clustering, from data preprocessing to visualization. It is especially useful for users who want to quickly prototype and analyze clustering results with minimal coding effort. For fine-tuned control, you can adjust DBSCAN parameters like eps and min_samples directly within PyCaret.






