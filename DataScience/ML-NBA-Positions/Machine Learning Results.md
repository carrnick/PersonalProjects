## Full Results
![best_score](https://user-images.githubusercontent.com/70597605/103489739-7a9e2980-4de4-11eb-8971-55eeb8e5481a.png)
![mean_fit_time](https://user-images.githubusercontent.com/70597605/103489747-81c53780-4de4-11eb-90e5-fb5f10699189.png)




## Gridsearch/Confusion Matrix
### *Decision Tree*
Parameters:

    param_grid = {"PCA__n_components" : [5, 7, 10, 12, 15] , 
             "PCA__whiten" : [True, False] , 
             "CLF__max_depth" : [3, 5, 10, 15] , 
             "CLF__criterion" : ['gini', 'entropy'] , 
             "CLF__max_features" : [5, 7, 9, 12, 15]}

![dc_res](https://user-images.githubusercontent.com/70597605/103489554-6279da80-4de3-11eb-8a1c-7cfbd08fa4eb.png)
![dc_conf](https://user-images.githubusercontent.com/70597605/103489553-6148ad80-4de3-11eb-8893-87a671ccc4cf.png)



### *Random Forest*
Parameters:

    param_grid = {'rf__n_estimators' : [200, 250], 
              'rf__max_depth' : [10, 12, 15, 17 ,20],
              'rf__min_samples_split' : [5, 7, 10]}

![rf_res](https://user-images.githubusercontent.com/70597605/103489636-f186f280-4de3-11eb-9d6f-85c2b3d71169.png)
![rf_conf](https://user-images.githubusercontent.com/70597605/103489638-f21f8900-4de3-11eb-9e17-42f0f070af3a.png)

### *K-Nearest Neighbors*
Parameters:

    param_grid = {"knn__n_neighbors" : np.arange(3, 26, 3),
               "knn__p" : [1, 2]}

![knn_res](https://user-images.githubusercontent.com/70597605/103489681-1da27380-4de4-11eb-933b-1017341d7c8e.png)

### *Support Vector Machine*
Parameters:

    param_grid = {
    'svm__C':np.arange(3, 15, 1),
    'svm__kernel' : ['rbf', 'poly']}
![svc_res](https://user-images.githubusercontent.com/70597605/103489686-25faae80-4de4-11eb-9203-cb5d5fe605f1.png)
