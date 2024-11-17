# Explore TimeGPT, Tabula9 and Relational Deep Learning

### Assignment:

Write colabs and run and  demonstrate in a video presentation the results of these runs explaining the colab what it does. be comprehensive explaining what is happening in the code. 

TimeGPT:

a) timegpt multivariate colab and long horizon colab  with example timeseries data
hint: https://docs.nixtla.io/docs/tutorials-multiple_series_forecasting

b) finetune timegpt with your own data - hint: https://docs.nixtla.io/docs/tutorials-fine_tuning

c) anomaly detection of timeseries using timegpt - hint : https://docs.nixtla.io/docs/tutorials-anomaly_detection

d) utilize timegpt for energy forecasting  - hint : https://docs.nixtla.io/docs/use-cases-forecasting_energy_demand

e) use timegpt for bitcoin forecasting :  hint : https://docs.nixtla.io/docs/use-cases-bitcoin_price_prediction

Tabular:

a) Generate synthetic data for a real data set   hint: https://github.com/zhaozilong/Tabula/blob/main/Tabula_on_insurance_dataset.ipynb
b) demonstrate inference on tabula model with zero shot hint: https://github.com/mlfoundations/rtfm/blob/main/notebooks/inference.ipynb

RDL and relbench:

a) in a colab,  train a gnn based model for tabular prediction task using relbench and show metrics - hint: https://relbench.stanford.edu/start https://colab.research.google.com/github/snap-stanford/relbench/blob/main/tutorials/train_model.ipynb

### Solution:

# TimeGPT:

Youtube Link: https://youtu.be/qANnp7KCYbA  

[![TimeGPT Features](https://img.youtube.com/vi/qANnp7KCYbA/0.jpg)](https://www.youtube.com/watch?v=qANnp7KCYbA) 

a) TimeGPT Multivariate: https://colab.research.google.com/drive/1PP1yPYbHuaEi-59DqHgYNIKYLpU1qply?usp=sharing 

   Long Horizon: https://colab.research.google.com/drive/1E2dEwkbI3EC3vuZQH0cV-koLAY8nyeji?usp=sharing 

b) Fine Tuning: https://colab.research.google.com/drive/19QigbecDe7SNJuEQ2mNncaXwFG02-loU?usp=sharing 

c) Anomaly Detection: https://colab.research.google.com/drive/1FeSkst1BiDl0wgN-zsnLLcbtALhemDhV?usp=sharing 

d) Energy Forecating: https://colab.research.google.com/drive/18j4_WMoNSro_8pdb7Za8aYbXNFGYhSyX?usp=sharing 

e) Bitcoin Forecating: https://colab.research.google.com/drive/1awgL02tHfXwIm5Y01aqBqCU4k9X53Lpa?usp=sharing 

# Tabula:

Generate synthetic data for a real data Colab Link: https://colab.research.google.com/drive/17LodfWhcxVVdShdYtJGeoPvyYIeFOtGY?usp=sharing

Inference on Tabula model with zero shot Colab Link: https://colab.research.google.com/drive/17LodfWhcxVVdShdYtJGeoPvyYIeFOtGY?usp=sharing

Youtube Link: 

# RDL and Relbench:

Colab Link: 

Youtube Link:

## Key Learnings:

# TimeGPT:

TimeGPT is a production-ready generative pretrained transformer for time series. It’s capable of accurately predicting various domains such as retail, electricity, finance, and IoT with just a few lines of code. It is user-friendly and low-code. Users can simply upload their time series data and generate forecasts or detect anomalies with just a single line of code.

#### Features and Capabilities:

Zero-shot Inference: TimeGPT can generate forecasts and detect anomalies straight out of the box, requiring no prior training data. This allows for immediate deployment and quick insights from any time series data.

Fine-tuning: Enhance TimeGPT’s capabilities by fine-tuning the model on your specific datasets, enabling the model to adapt to the nuances of your unique time series data and improving performance on tailored tasks.

API Access: Integrate TimeGPT seamlessly into your applications via our robust API (obtain an API key through our Dashboard). TimeGPT is also supported through Azure Studio for even more flexible integration options. Alternatively, deploy TimeGPT on your own infrastructure to maintain full control over your data and workflows.

Add Exogenous Variables: Incorporate additional variables that might influence your predictions to enhance forecast accuracy. (E.g. Special Dates, events or prices)

Multiple Series Forecasting: Simultaneously forecast multiple time series data, optimizing workflows and resources.

Specific Loss Function: Tailor the fine-tuning process by choosing from many loss functions to meet specific performance metrics.

Cross-validation: Implement out of the box cross-validation techniques to ensure model robustness and generalizability.

Prediction Intervals: Provide intervals in your predictions to quantify uncertainty effectively.

Irregular Timestamps: Handle data with irregular timestamps, accommodating non-uniform interval series without preprocessing.

Anomaly Detection: Automatically detect anomalies in time series, and use exogenous features for enhanced performance.

# Tabula:

Tabula improves tabular data synthesis by leveraging language model structures without the burden of pre-trained model weights. It offers a faster training process by preprocessing tabular datato shorten token sequence, which sharply reducing training time while consistently delivering higher-quality synthetic data.

# Relational Deep Learning:

Relational Deep Learning is a new approach for end-to-end representation learning on data spread across multiple tables, such as in a relational database. Relational databases are the world’s most widely used data management system, and are used for industrial and scientific purposes across many domains. RelBench is a benchmark designed to facilitate efficient, robust and reproducible research on end-to-end deep learning over relational databases.

RelBench contains 7 realistic, large-scale, and diverse relational databases spanning domains including medical, social networks, e-commerce and sport. Each database has multiple predictive tasks (30 in total) defined, each carefully scoped to be both challenging and of domain-specific importance. It provides full support for data downloading, task specification and standardized evaluation in an ML-framework-agnostic manner. Additionally, RelBench provides a first open-source implementation of a Graph Neural Network based approach to relational deep learning. This implementation uses PyTorch Geometric to load the data as a graph and train GNN models, and PyTorch Frame for modeling tabular data.




