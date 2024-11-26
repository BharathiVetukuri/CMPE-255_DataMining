# Assignment:

a) K-Means clustering from scratch

hint : https://colab.sandbox.google.com/github/SANTOSHMAHER/Machine-Learning-Algorithams/blob/master/K_Means_algorithm_using_Python_from_scratch_.ipynb.

or https://colab.sandbox.google.com/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/05.11-K-Means.ipynb.

another interesting supervised kmeans colab if people like to do : https://developers.google.com/machine-learning/clustering/programming-exercise.

https://colab.sandbox.google.com/github/google/eng-edu/blob/main/ml/clustering/clustering-supervised-similarity.ipynb?utm_source=ss-clustering&utm_campaign=colab-external&utm_medium=referral&utm_content=clustering-supervised-similarity#scrollTo=eExms-TP8Hn6

# Solution:

Colab Links: https://colab.research.google.com/drive/1sW9U99LLa4yDR5H8i_YP2zUXcqEdCTUl?usp=sharing 
             https://colab.research.google.com/drive/1IqxOdSLWzbplz1ZjqQEK6NiEmxvgfHtn?usp=sharing 

Yotube Link: https://youtu.be/oVuzOKmwBk0 

### Key Learnings:

## **Clustering and K-Means:**

Clustering is the process of grouping similar data points together based on their features. Each group is called a cluster, and the goal of clustering is to ensure that:

Data points in the same cluster are similar to each other.
Data points in different clusters are dissimilar.

K-Means is one of the most popular unsupervised machine learning algorithms for clustering data into groups.

### **How K-Means Works**:
Choose the Number of Clusters (k): Decide how many groups (clusters) you want to divide the data into.

Initialize Cluster Centroids: Randomly select k points in the dataset as the initial cluster centroids (representative points for each cluster).

Assign Points to Nearest Centroid: For each data point, calculate its distance to each centroid and assign it to the nearest one.

Update Centroids: Recalculate the centroids by taking the mean of all points assigned to a cluster.

Repeat: Repeat steps 3 and 4 until the centroids stop changing significantly or a maximum number of iterations is reached.

### **Methods to Determine the Optimal Number of Clusters**

#### 1. The Elbow Method
The Elbow Method plots the inertia (sum of squared distances of points to their cluster centroids) against the number of clusters (k). The "elbow point" is where adding more clusters provides diminishing returns.

#### 2. The Silhouette Score
The Silhouette Score measures how well data points fit into their clusters. Scores range from -1 to 1, where higher values indicate better clustering.

#### Elbow Curve:
The Elbow Curve is a graphical method used in K-Means clustering to determine the optimal number of clusters (k). It involves plotting the inertia (also called within-cluster sum of squares) against the number of clusters and identifying the "elbow point" where the rate of decrease slows significantly.


