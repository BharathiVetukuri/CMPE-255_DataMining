# Decision Trees
A Decision Tree is a supervised learning algorithm used for classification and regression tasks. It works by recursively splitting the dataset into subsets based on feature values, forming a tree-like structure. The tree is constructed in a top-down approach, starting from the root node and branching out to leaf nodes, which represent the final predictions.

### Key Concepts in Decision Trees

**Tree Structure:** The decision tree is made up of nodes and branches.

* Root Node: The topmost node representing the feature that provides the maximum information gain or minimum impurity.

* Internal Nodes: Represent features used for further splitting.

* Leaf Nodes: Represent the final predicted outcome.

**Splitting Criteria:** The algorithm chooses splits based on measures like:

* Gini Index: Measures impurity. Lower values are better.
  
* Entropy/Information Gain: Measures reduction in uncertainty.
  
* Variance Reduction: Used in regression trees to minimize variance in subsets.
  
* Recursive Partitioning: The tree-building process continues recursively until a stopping condition is met (e.g., maximum depth, minimum samples per node).

### Steps in Decision Tree Learning
Start with the Entire Dataset: The root node is created using all the training data.

Select the Best Split:

Evaluate all possible splits for each feature.
Choose the feature and threshold that result in the maximum information gain or lowest impurity.
Partition the Data: Split the dataset into subsets based on the chosen feature and threshold.

Repeat for Each Subset: Create child nodes by recursively applying the splitting process.

Stop When a Stopping Condition is Met: The tree stops growing when:

All data in a node belong to the same class.
Maximum tree depth is reached.
The minimum number of samples per node is below a threshold.
Advantages of Decision Trees
Interpretability: Easy to visualize and understand.
Non-linearity: Captures non-linear relationships in data.
No Need for Feature Scaling: Handles raw data effectively.
Disadvantages of Decision Trees
Overfitting: Prone to overfitting if the tree grows too deep.
Bias in Splitting: Can favor features with more levels (categorical features).
Instability: Small changes in data can lead to significant changes in the tree structure.
Comparison with Other Methods
Random Forest: Unlike a single decision tree, a random forest builds multiple trees (ensemble) and aggregates their predictions to reduce overfitting.
AdaBoost: Combines multiple weak decision trees sequentially, focusing on misclassified samples to improve accuracy.
Gradient Boosting: Similar to AdaBoost but optimizes the splits using gradient descent methods.
