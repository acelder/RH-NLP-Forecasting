# RH-NLP-Forecasting

This project seeks to predict RobinHood popularity scores using natural language processing via AWS SageMaker. See the exploratory/ folder 
for an examination of the input and target data, the processing/ folder for data processing, and training/ for model training and limited 
deployment. The most interesting notebooks are training/training-pytorch.ipynb and exploratory/explore-rh-popularity.ipynb. 

This is a side project I've been working on on-and-off for a couple of years. Files included here represent the components of the analysis 
that I've taken the time to spruce up. I may add additional work as I have time to review and properly document it.

Dependencies

In addition to the standard Python ML stack (numpy, pandas, scikit-learn), Pytorch was used for
deep learning models and Sagemaker’s LinearLearner class was used for linear bag of words
sentiment models.
NLTK was used for text preprocessing.
The yahoo finance api yfinance was used for market data.

Model Files

Data was retrieved from sources and processed locally prior to uploading to S3 for model
training. Notebooks related to this work as well as establishment of naive benchmarks and
market-based benchmark models can be found in the local source directory.
Two separate model strategies, bag of words classifier and LSTM, were implemented in AWS
sagemaker. These files can be found in the training/ directory.

Data

Data was retrieved from sources and processed locally prior to uploading to S3 for model training. Raw and processed data files 
are not included. Raw data for the NLP models was sourced from the URLs below. Google cloud’s bigquery was
used to retrieve post data from the pushshift records. Benchmark market data was obtained from Yahoo Finance.
Stock popularity: https://www.kaggle.com/cprimozi/robinhood-stock-popularity-history
Post history: https://files.pushshift.io/
