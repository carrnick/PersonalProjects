# Reuters Headlines Analysis
Sentiment analysis of Reuters news headlines using Sklearn's [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) to determine if headlines can predict if the S&P500 closed higher than the previous day.

[Full Code](https://github.com/carrnick/Reuters-Headlines-Analysis/blob/main/Reuters_S%26P.ipynb)

### Quick Results:  
 
| Model | Accuracy Score  | F1-Score | AUC-Score |
|------------------------------|----------|---------|-
|**Random Forest Classifier**  | 67.6%  | 72.2% | 74.9% |
| **XGBoost** | 63.2% | 72.1% | 68.7%
|**LSVM** | 67.1% | 72.2 % | 68.7%  

  --------------------------------------------------
| Model | TPR  |  FPR|
|------------------------------|----------|---------|
|**Random Forest Classifier**  | 71.6%  | 34.5% |
| **XGBoost** | 59.2% | 30.4%| 
|**LSVM** | 78.2% | 36.8%% | 


# Methodology
1) Get data of each Reuters headline and the date posted.
2) Transform dataset so each row contains a date and list of headlines for that date.
3) Use [yfinance](https://pypi.org/project/yfinance/) to get price history for the S&P 500.
4) Merge pricing history and headlines together, resulting in a dataset containing a date, list of headlines, and closing price for each date.
5) Loop through dataset and assign labels to each row. The label is 1 if the S&P 500 closed higher than the previous day, and 0 otherwise.
6) Pass list of headlines into TfidfVectorizer (this will be broken down later).
7) Use machine learning models to determine if headlines can predict if the S&P 500 closed higher than the previous day.
8) Analyze models with Confusion Matrices, ROC Curve, and Precision-Recall Curve.

# Examples of Data

The original data contains each headline posted on Reuters between March 20, 2018 and June 18, 2020.
![Capture](https://user-images.githubusercontent.com/70597605/104619492-ec376c80-565b-11eb-8975-75c269b99d90.PNG)

In order to effectively use TfidfVectorizer, the headlines need to be put into a string containing each headline for the respective date. This was accomplished by grouping by day, then transforming the headlines to a list of each headline.

***Example of headlines from March 3, 2020:***

![Capture](https://user-images.githubusercontent.com/70597605/104619670-26087300-565c-11eb-85dc-f31892c46896.PNG)

Next, data of the S&P 500 is retrieved using Python's yfinance library:

![Capture](https://user-images.githubusercontent.com/70597605/104620002-7d0e4800-565c-11eb-8587-feb68afc21e2.PNG)

Finally, the data is labeled and merged together.

![Capture](https://user-images.githubusercontent.com/70597605/104620186-b5ae2180-565c-11eb-8777-f395a870eba6.PNG)

***Count of Labels***

![fig](https://user-images.githubusercontent.com/70597605/104623219-273b9f00-5660-11eb-9b4c-479b9beb890d.png)

# TfidfVectorizer
Sklearn's [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) converts a collection of raw documents (strings in this case) to a matrix of TF-IDF features.   

A TF-IDF feature is a statistical measure that evaluates how relavant a word is to a document. The library will find how many times a word appears in a document, and multiplies it by the inverse frequency of the words across the document.  

Esentially, the goal is to use TfidfVectorizer to find common words that appear when the market closes higher than the previous day, and use a machine learning model to determine which words are most relevant.


***Sample of most common groups of two words:***
![freq](https://user-images.githubusercontent.com/70597605/104620825-69afac80-565d-11eb-9444-11315b314bfa.png)

***Most common singular words:***
![freq](https://user-images.githubusercontent.com/70597605/104620990-9cf23b80-565d-11eb-8e93-ed3911878bc3.png)
# Machine Learning Models and Results


## Random Forest Classifier

> - Best performer out of the three models
>  - 72% TPR,  65% TNR


*Confusion Matrix*

![confmatrf](https://user-images.githubusercontent.com/70597605/104616475-53ebb880-5658-11eb-95dd-49bbb82a7835.png)

*ROC Curve*

![rfrocauc](https://user-images.githubusercontent.com/70597605/104617213-2c492000-5659-11eb-96dd-3c5dd076fc68.png)

*Precision-Recall Curve*

![prcurve_rf](https://user-images.githubusercontent.com/70597605/104616414-446c6f80-5658-11eb-8294-7cd6b4b67fcf.png)

*Accuracy Scores*

![rfmeasures](https://user-images.githubusercontent.com/70597605/104617209-2b17f300-5659-11eb-9542-d95a68d2cc9c.png)



## XGBoost
> - Worst overall performer out of the three models, however it was surprisingly effective at predicting "Up" labels, and had the highest TNR
>  - 59% TPR,  78% TNR
>  
*Confusion Matrix*

![confmatxg](https://user-images.githubusercontent.com/70597605/104616797-bc3a9a00-5658-11eb-83c1-07d4298462b3.png)

*ROC Curve*

![xgra](https://user-images.githubusercontent.com/70597605/104616796-bba20380-5658-11eb-9597-98fd73513252.png)

*Precision-Recall Curve*

![xgpr](https://user-images.githubusercontent.com/70597605/104616795-bba20380-5658-11eb-9d99-ad7caf479180.png)

*Accuracy Scores*

![xgclass](https://user-images.githubusercontent.com/70597605/104616794-bba20380-5658-11eb-9aee-37b5a60d4c3f.png)

## Linear Support Vector Machine
> - Extremely effective TPR, but below average TNR
> - 78.2% TPR, 63.1% TNR
> 
*Confusion Matrix*

![Capture](https://user-images.githubusercontent.com/70597605/104622662-8baa2e80-565f-11eb-9614-f550242ad7a8.PNG)


*ROC Curve*

![lsvmra](https://user-images.githubusercontent.com/70597605/104617266-3cf99600-5659-11eb-8053-3456be72b657.png)

*Precision-Recall Curve*

![lvsmprc](https://user-images.githubusercontent.com/70597605/104617265-3c60ff80-5659-11eb-865a-35e6eeda6e0e.png)

*Accuracy Scores*

![lsvmmeasures](https://user-images.githubusercontent.com/70597605/104617263-3c60ff80-5659-11eb-90a2-8d2bd633fcfd.png)



# Summary
*For our sample size, there is definitely value by scraping news headlines. Both the Random Forest and LSVM models have a significant capability to predict whether the S&P 500 will close higher than the previous day. The XGBoost model also does better than average, but with a weak Precision-Recall Curve, it is not on the same level as Random Forest or LSVM. The next steps would be to get more data of headlines from different news sources, try different stock indexes, and try to predict the exact price of the stock based on the times of articles.*
