# Predicting an NBA Player's Position 
## Project Goal
 *The NBA is considered the most "positionless" major sport. The game has evolved to the point where 6'8" players could play any position, from guard to center. Can machine learning be used to predict an NBA player's position based on their in-game stats?*

### Data
> [NBA Player's Stats since 1950](https://www.kaggle.com/drgilermo/nba-players-stats)

### Libraries Used
> - Pandas
> - Numpy
> - Sklearn

### Machine Learning Algorithms Used
> - Decision Trees
> - Random Forest
> - K-Nearest Neighbors
> - Support Vector Machine


## Results
*To see all code, plots, and data, click [here](https://github.com/carrnick/ML-for-NBA-Players-Positions/blob/main/all.pdf).*  
*To see all machine learning results, click [here](https://github.com/carrnick/ML-for-NBA-Players-Positions/blob/main/Machine%20Learning%20Results.md).*

![best_score](https://user-images.githubusercontent.com/70597605/103489443-9b657f80-4de2-11eb-9736-7f9e341f8c8a.png)
> - *Decision Tree* : 79.21% accuracy
>  - *Random Forest* : 91.34% accuracy 
>  - *KNN* : 87.19% accuracy
>  - *SVM* : 84.52% accuracy



## EDA Plots
*To zoom in, just click the plot*

![dist1](https://user-images.githubusercontent.com/70597605/103489207-b7682180-4de0-11eb-8fec-3b9f4c481102.png)
- Distribution of AST% and STL% by position
![dist2](https://user-images.githubusercontent.com/70597605/103489356-095d7700-4de2-11eb-820d-0962d0c057f1.png)
- Distribution of FGA and MP
![dist3](https://user-images.githubusercontent.com/70597605/103489358-0bbfd100-4de2-11eb-94d2-b470bbe44b63.png)
- Distribution of height and weight by position
![dist4](https://user-images.githubusercontent.com/70597605/103489359-0cf0fe00-4de2-11eb-811e-f392bc847d51.png)
- Frequency of 3PAr, TRB%, ORB%, and DRB% by position
![dist5](https://user-images.githubusercontent.com/70597605/103489361-0e222b00-4de2-11eb-8dff-c2bd7baab22d.png)
- Most important features![kbest](https://user-images.githubusercontent.com/70597605/103489824-2778a680-4de5-11eb-93ea-8aac49117676.png)
