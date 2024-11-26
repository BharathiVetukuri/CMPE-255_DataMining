# Clustering of Timeseries Data using Pretrained Models 

Hint : 

https://github.com/V-MalM/Stock-Clustering-and-Prediction

https://github.com/qianlima-lab/time-series-ptms

https://github.com/effa/time-series-clustering

https://github.com/qingsongedu/Awesome-TimeSeries-SpatioTemporal-LM-LLM

https://github.com/cure-lab/Awesome-time-series#time-series-clustering

https://github.com/qingsongedu/awesome-AI-for-time-series-papers

# Solution:

Colab Link: https://colab.research.google.com/drive/1890Fijz9VPLSkMQFPjtv768dAefT1wyD?usp=sharing 
            https://colab.research.google.com/drive/1g-nmAOJ-c1JtaBP2hL8aszKDPNMp4FOD?usp=sharing

Youtube: https://youtu.be/TjuMXaL0k7Y 

[![TimeSeries](https://img.youtube.com/vi/TjuMXaL0k7Y/0.jpg)](https://www.youtube.com/watch?v=TjuMXaL0k7Y) 

### Key Learnings:

## TimeSeries Clustering

Clustering time series data using pretrained models involves grouping similar time series based on learned representations, typically obtained from models trained to capture temporal patterns.

##### Steps for Clustering Time Series Data Using Pretrained Models

#### 1. Preprocessing the Time Series Data

**Normalization/Standardization:** Scale the data to ensure uniformity.

**Resampling:** Ensure all time series have the same length (e.g., via interpolation or truncation).

**Noise Removal:** Apply smoothing techniques like moving averages if necessary.

#### 2. Extract Features Using Pretrained Models
Pretrained models capture meaningful patterns and characteristics of time series data, enabling clustering based on extracted features.

**Common Pretrained Models:**

**a. Autoencoders:**

Train an autoencoder to compress time series into lower-dimensional latent vectors.
Use the encoder part of a pretrained autoencoder for feature extraction.

**b. Convolutional Neural Networks (CNNs):**

Models trained for classification tasks (e.g., image or time series) can be fine-tuned or directly used to extract embeddings.

**c. Recurrent Neural Networks (RNNs) / LSTMs / GRUs:**

RNN-based models capture temporal dependencies and can be used to generate embeddings.

**d. Transformers:**

Pretrained transformers (like Time2Vec or models fine-tuned for time series) encode positional and sequential information effectively.

**e. Dynamic Time Warping (DTW)-based Representations:**

DTW measures similarity between time series. Pretrained DTW-based methods may provide alignment metrics or distance matrices.

**f. Feature-Based Libraries:**

Libraries like tsfresh or catch22 compute handcrafted statistical features from time series data.

#### 3. Clustering
Once features are extracted using a pretrained model, clustering methods like k-means or hierarchical clustering are applied.






