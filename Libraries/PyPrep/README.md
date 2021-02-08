# PyPrep
> A wrapper around Pandas and Sklearn that makes data cleaning and preprocessing quicker and easier.  
> To see code along with documentation, read the [pdf version of the documentation](https://github.com/carrnick/PyPrep/blob/main/documentation.pdf)


## Initialization
*Parameters*: 

 - `data` : Pandas.DataFrame
 - `copy` : Boolean, default True
 - `y` : String, default None

## Functions
`PyPrep.head()`
>  Wrapper around Pandas head method


`PyPrep.get_numeric()`
 > Returns the numeric columns in the dataframe in list form
 
 
`PyPrep.get_categorical()`
> Similar to *get_numeric()*, but returns a list of categorical columns


`PyPrep.get_missing(*type = 'list'*)`
Parameters: 
 - `type :  String: list, heatmap, percentage`
> *If type is "list", the method returns a list of null values for each column*  
> *If type is "heatmap", the method returns a heatmap of null values for each column*  
> *If type is "percentage", the method returns a bar plot of null values in each column*


`PyPrep.get_duplicates(*plot = False*)`
Parameters: 
 - `plot :  Boolean`
> *Returns the number of duplicate values in each column*  
> *If `plot` is True, the method returns a barplot of the number of duplicate values in each column*  


`PyPrep.get_zscore(*columns = None, threshold = 3*)`
Parameters: 
 - `columns : List of Columns`
 - `threshold` :  Integer
> *Calculates the z-score of each numeric column in the DataFrame*  
> *Returns rows where the z-score is greater than or equal to `threshold` argument*  


`PyPrep.get_repetitive(*threshold = .95*)`
Parameters: 
 - `threshold :  Float <= .99`
> *Returns columns that have reptitive values greater than or equal to `threshold` argument*  


`PyPrep.select_best(*columns, k = 5, dtype = 'numeric', plot = False*)`
Parameters: 
 - `columns :  List of Columns`
 - `k** : Number of variables to select`
 - `dtype** : String : 'numeric' or 'categorical'`
 - `plot** : Boolean`
> *Wrapper around Sklearn  [SelectKBest](https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html)*  
> *Selects `k` most statistically significant rows*


`PyPrep.corr_plot()`
> *Returns a correlation plot between numeric values and target variable*


`PyPrep.encode(*columns = None, method = 'onehot', drop = False)`
Parameters: 
 - `columns :  List of Columns`
 - `method: String : 'onehot' or 'label'`
 - `drop : Boolean` 
> *Wrapper around [OneHotEncoding](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html) or [LabelEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html)*  
