# Fraud Detection with Keras

[Data](https://www.kaggle.com/mlg-ulb/creditcardfraud)

## *Summary* 
- Applied TensorFlow model to a significantly imbalanced dataset of fraudulent transactions (~250,000 non-fradulent transactions, ~450 fradulent transactions)
- Solved imbalanced dataset problem by creating a balanced dataset, with an equal number of fraudulent and non-fraudulent transactions
- Used correlation matrix and boxplots on balanced dataset to find variables that contribute most to being fraudulent
- Removed outliers from the highest correlated features using Inter-Quartile Range (IQR)


## *Results*
- **Percentage of Fraud Caught (TNR): % 99.971**
- **Percentage of Fraud Missed (FPR): % 0.029**

## *EDA*

*Correlation Matrix of Balanced Dataset*

![equalcorr](https://user-images.githubusercontent.com/70597605/104377432-7f559280-54f4-11eb-82f8-e4d793972020.png)

*Plot of Correlation Scores*

![highestcorr](https://user-images.githubusercontent.com/70597605/104377463-8bd9eb00-54f4-11eb-8e33-2bca1fe77777.png)

*Variables with High/Low Correlation. Used to determine which features we should remove outliers from*
![lowcorr](https://user-images.githubusercontent.com/70597605/104379575-a6619380-54f7-11eb-9dde-afb3399e0cbc.png)
![highcorr](https://user-images.githubusercontent.com/70597605/104379576-a6fa2a00-54f7-11eb-9b0e-cbf265fa7ee3.png)


*Final Confusion Matrix*

![confmat](https://user-images.githubusercontent.com/70597605/104377490-985e4380-54f4-11eb-95c7-d5217fd58cae.png)
