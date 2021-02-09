# State Income and Firearm Murders

## Goal:
Analyze the relationship between state population and firearm murder in the United States between 2000 and 2010.

## Methodology:
**Independent Variables**: % of Murders Committed with Firearm (by year and state), Firearm Murders per 100k (by year and state)

**Dependent Variable**: Median Income (by year and state)

**Data**:
 [2000-2010 State Population](https://www2.census.gov/programs-surveys/popest/datasets/2000-2010/intercensal/state/)
[Homicide Reports 1980-2014](https://www.kaggle.com/murderaccountability/homicide-reports)
[Household Income by State](https://data.world/garyhoov/household-income-by-state)

**Model**: Linear Regression is used to determine the relationship between the independent and dependent variables.

## EDA
**Average % of Murders Committed with Firearm, by State**
![stateshighlow2](https://user-images.githubusercontent.com/70597605/107383833-60c8c400-6abf-11eb-9770-e36aef873d42.png)
**Average Firearm Murders per 100k, by State**
![stateshighlow](https://user-images.githubusercontent.com/70597605/107383885-71793a00-6abf-11eb-9baf-eb22b5e887fc.png)

**Average Income, Binned by Firearm%**
![firearm%_bin](https://user-images.githubusercontent.com/70597605/107383944-7fc75600-6abf-11eb-82fb-94771299b631.png)

**Average Income, binned by Firearm Murders/100k**
![firearm_100k_bin](https://user-images.githubusercontent.com/70597605/107384002-8e157200-6abf-11eb-9a7f-02784ceef7ca.png)

**Correlation Matrix**
![corr](https://user-images.githubusercontent.com/70597605/107384049-9b326100-6abf-11eb-90e3-92d668c36733.png)
## Results

**% of Murders Committed with Firearm and Income** 
![firearmpctreg](https://user-images.githubusercontent.com/70597605/107382884-670a7080-6abe-11eb-8cf9-8ecf4026f4c7.PNG)
![Firearm%~Income](https://user-images.githubusercontent.com/70597605/107383174-bc468200-6abe-11eb-9a93-ed296d6fb192.png)

**Firearm Murders per 100k and Income**
![firearm100kreg](https://user-images.githubusercontent.com/70597605/107382887-67a30700-6abe-11eb-9709-ecad240cf2e2.PNG)
![Firearm_100k~Income](https://user-images.githubusercontent.com/70597605/107383186-bf417280-6abe-11eb-9274-ad483a8b7237.png)

In both cases, there is slight evidence of a relationship. The stronger relationship is between Firearm Murders per 100k and Income, with a .05 R-Squared value and a P-Value of essentially 0. This means that Firearm Murders per 100k explains about 5% of the variance of Income, which leads to the conclusion that firearm crime has a slight impact on median income.
