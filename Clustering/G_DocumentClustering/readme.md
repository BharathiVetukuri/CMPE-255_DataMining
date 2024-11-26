# Clustering  of Documents using State of Art Embeddings (LLM Embeddings)

Colab Link: https://colab.research.google.com/drive/1M1xTPxZqLndH0GgSActKeYjiwUqJbAT6?usp=sharing 

Yotube: https://youtu.be/Pp8MnlCKpgE 

[![DocumentClustering](https://img.youtube.com/vi/Pp8MnlCKpgE/0.jpg)](https://www.youtube.com/watch?v=Pp8MnlCKpgE) 

### Key Learnings:

## Document Clustering using State of Art Embeddings

Clustering documents using state-of-the-art embeddings, particularly from large language models (LLMs) like GPT, BERT, or their derivatives, can significantly improve the quality of clustering. These models can provide dense, semantically rich vector representations of text, which capture the underlying meaning, context, and relationships between words or phrases in a document.

### Step to cluster documents using state-of-the-art embeddings from LLMs:

**1. Install Required Libraries:** To work with LLMs, you need libraries like Transformers for easy access to pretrained models, sentence-transformers for generating embeddings, and scikit-learn for clustering algorithms.

**2. Load Pretrained Language Model for Embeddings:** You can use models like BERT, RoBERTa, or Sentence-BERT to generate embeddings. Sentence-BERT (SBERT) is specifically optimized for sentence or document-level embeddings and is often a good choice.

**3. Prepare Your Documents:** Prepare the documents you want to cluster. This can be a list of texts (each text being a document or sentence).

**4. Generate Embeddings for the Documents:** Use the pretrained model to encode your documents into dense vector embeddings.

**5. Cluster the Documents:** A common choice for document clustering is K-Means, but other algorithms such as DBSCAN, Agglomerative Clustering, or HDBSCAN might also be effective, especially if you have noisy or non-globular clusters.

**6. Evaluate the Clustering:** While evaluating unsupervised clustering is challenging, there are some metrics that can help assess the quality of your clusters:

**Silhouette Score:** Measures how similar each document is to its own cluster versus other clusters.

**Adjusted Rand Index (ARI):** If you have ground truth labels.

**Calinski-Harabasz Index:** Measures the variance between clusters.

Clustering documents using state-of-the-art embeddings from LLMs like Sentence-BERT provides a powerful way to group similar documents based on their semantic content. This approach is robust and scalable, making it suitable for a wide range of text clustering applications, from news categorization to legal document clustering and beyond.
