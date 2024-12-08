# AdaBoost (Adaptive Boosting) 

AdaBoost is an ensemble learning algorithm that combines multiple weak learners (typically decision stumps or shallow trees) to form a strong classifier. It focuses on the instances that are harder to classify by adjusting their weights iteratively during training.

# Key Concepts in AdaBoost Boosting:

A sequential learning process where each new model is trained to correct the errors of its predecessor. 

**Weak Learner:** A model that performs slightly better than random guessing (e.g., decision stumps). 

**Adaptive Weighting:** AdaBoost assigns higher weights to misclassified samples, making them more significant in the next iteration. Each weak learner is given a weight based on its accuracy, and these weights are used to combine the predictions. 

**Final Prediction:** The final model combines the weighted predictions of all weak learners. 

# Steps in AdaBoost 

**Initialize Sample Weights:** Assign equal weights to all training samples initially. 

**Iterative Weak Learner Training:**

At each step: 

* Train a weak learner using the current sample weights. 
* Compute the weighted error of the weak learner. 
* Calculate the learner's weight based on its error.

**Update the sample weights:** increase weights for misclassified samples, decrease for correctly classified ones. 

**Combine Weak Learners:** The final prediction is a weighted majority vote (classification) or a weighted sum (regression). 

# Advantages of AdaBoost 

**High Accuracy:** Combines multiple weak learners into a strong classifier. 

**Versatility:** Works well with a variety of base learners and datasets. 

**Focus on Hard Samples:** Adaptive weighting ensures that difficult samples are prioritized.

# Comparison with Other Methods 

* Unlike Random Forest, which trains trees independently, AdaBoost trains weak learners sequentially, focusing on improving the performance on misclassified samples. 
* Advanced variants like Gradient Boosting and XGBoost improve on AdaBoost by incorporating gradient-based optimization and better handling of data.
