# Image Clustering using Imagebind LLMs

Colab Link: https://colab.research.google.com/drive/1_C2FGzH9a9owo0mMUJZGxwRH2Wbz9mh8?usp=sharing 

Youtube: https://youtu.be/IN6Ufo6xTk8 

[![ImageClusteringAudioEmbeddings](https://img.youtube.com/vi/IN6Ufo6xTk8/0.jpg)](https://www.youtube.com/watch?v=IN6Ufo6xTk8) 

### What is ImageBind?

ImageBind is a framework by Meta that enables creating embeddings for various modalities (audio, text, image, etc.) into a shared embedding space. ImageBind enables embeddings for:

* Audio
* Text
* Image
* Depth
* Thermal (infrared)
* IMU (motion sensors)

It maps these modalities to a unified latent space, making it useful for cross-modal tasks

### Step-by-Step Workflow for Image Embeddings with ImageBind and LLMs

Clustering images using ImageBind embeddings is a powerful technique for grouping similar images in a shared embedding space. ImageBind maps images (and other modalities) into a unified latent space, making clustering straightforward after embedding extraction.

**1. Install and Set Up ImageBind:** Install the ImageBind library and its dependencies for ImageBind, clustering, and visualization.

**2. Extract Image Embeddings Using ImageBind:** Load ImageBind model and process images and generate embeddings

**3. Perform Clustering:** Choose an appropriate Clustering method.

**4. Visualize Clustering Results:** Once you have the clustering results, visualize them.
