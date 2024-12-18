# Data engineering and Apache Beam or Apache Spark

### Assignment:
a) Assignment 1 is to do a complete dataset EDA in colab (preferably using D3.js visualizations)
Pick a complex dataset from kaggle 
Please push to limits and demonstrate advanced d3.js visualizations 

b) Assignment 2 - Auto EDA with your favorite tool
Pick your favorite kaggle data set and favorite auto eda tool (like pandas profiler or sweetviz etc.,.) 
Do auto eda using one of the tools i discussed in the class which is your favorite. make it very appealing for viewers

c) Assignment 3 - Apache beam features - demonstrate apache beam in a colab including composite transform, pipeline io, triggers, windowing ,pardo and streaming
https://beam.apache.org/documentation/programming-guide/Links to an external site.
create a video explaining above works 
You can useBeamML for exercise https://beam.apache.org/documentation/ml/about-ml/Links to an external site.

### SOLUTION:

Youtube Link: https://youtu.be/V1YApPvBdWs 

[![Apache Beam](https://img.youtube.com/vi/V1YApPvBdWs/0.jpg)](https://www.youtube.com/watch?v=V1YApPvBdWs)

#### a) EDA (Exploratory Data Analysis):

EDA stands for Exploratory Data Analysis. It is a crucial step in the data analysis process, during which a data analyst or data scientist explores and visualizes data sets to understand their main characteristics, often using statistical graphics and other data visualization methods. Here are the primary goals and steps involved in EDA:

##### Goals of EDA:
Discover Patterns: Identify patterns, trends, and relationships among data points.
Spot Anomalies: Detect outliers and anomalies that might skew the data or indicate data errors.
Frame Hypotheses: Formulate hypotheses and questions based on the visualization and understanding of the data.
Check Assumptions: Verify assumptions used in statistical models for further analysis or predictive modeling.
Prepare for Further Analysis: Prepare data for further processing, including cleaning and feature engineering, which are crucial for predictive modeling.

EDA is generally the first step in the data modeling process, right after initial data cleaning and preparation, and it guides how to proceed with predictive modeling or other advanced data analysis tasks. It is largely an open-ended process and can vary significantly from one analysis to another based on the data and the specific questions being asked.

Colab Link: https://colab.research.google.com/drive/18MJos619waWgh-9xjgBlV-L9rCisPtOB?usp=sharing 

#### b) AUTO EDA with Pandas Profiler:

For this part of the assignment I have chosen Pandas Profiler tool to perform EDA. Auto EDA (Exploratory Data Analysis) tools can significantly speed up the data analysis process by automating many of the routine tasks involved in exploring datasets. Pandas Profiling is one such tool that integrates with Python and the pandas library to create detailed statistical reports from a DataFrame.

Auto EDA with Pandas Profiler streamlines the initial data exploration process by automatically generating comprehensive reports from pandas DataFrames. This tool provides detailed insights into each dataset, including distributions, correlations, missing values, and more, all through a single line of code. The generated reports are interactive and include visualizations for a deeper understanding of the data, making Pandas Profiler an essential tool for quickly assessing data quality and structure. This efficiency is invaluable in large datasets, helping analysts and data scientists to identify potential areas of focus or concern at the outset of their analysis.

Colab Link: https://colab.research.google.com/drive/10DyxmrJUGHl6H0E416iaT-BeHs2SC84j?usp=sharing 

Report Recording Link: https://youtu.be/CQ-nLRSjOrE 

[![EDA Report Recording](https://img.youtube.com/vi/CQ-nLRSjOrE/0.jpg)](https://www.youtube.com/watch?v=CQ-nLRSjOrE)


#### c) APACHE BEAM FEATURES:

Apache Beam is a powerful tool for building parallel data processing pipelines, with several advanced features to handle complex processing tasks for both batch and stream data. Demonstrated the following Features of Apache Beam in the cloab: composite transform, pipeline io, triggers, windowing ,pardo and streaming.

##### 1. ParDo
ParDo is one of the most fundamental processing primitives in Apache Beam, similar to the "map" or "flatMap" functions in other data processing systems. It processes each element of the input independently and can produce zero or more output elements, allowing for operations such as filtering, updating, and transforming elements.

##### 2. Composite Transforms
Composite transforms are user-defined combinations of multiple transforms that bundle processing logic into a single module. This allows for reusable components and cleaner code.

##### 3. Windowing
Windowing is used to subdivide a PCollection according to the timestamps of its individual elements. Beam supports several windowing strategies like fixed, sliding, session, and global windows.

##### 4. Triggers
Triggers in Beam allow the system to handle late data by specifying when to emit the results of a window. Triggers can fire based on processing time, data arrival, or after a certain delay.

##### 5. Pipeline I/O
Beam supports reading from and writing to various data sources and sinks. This includes files, databases, and message queues, which allows Beam to interact with external systems seamlessly.

##### 6. Streaming
Beam excels at handling streaming data, providing real-time data processing capabilities by continuously updating the results as new data arrives.

Each of these features makes Apache Beam a robust choice for complex data processing tasks, enabling scalable and efficient implementations for both batch and real-time streaming applications.

Colab Link: https://colab.research.google.com/drive/1chxZ9y3OKH6J_GaEPB9pt5pwxn0OX9nm?usp=sharing 





