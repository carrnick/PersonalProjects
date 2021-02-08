# The Effect of Climate on City Crime
Regression analysis and hypothesis tests for average temperature/rainfall in New York City, and how it relates to the frequency of crime.

[All Code and Plots](https://github.com/carrnick/The-Effect-of-Climate-on-City-Crime/blob/main/The%20Effect%20of%20Temperature%20on%20NYC%20Crime.ipynb)


![summer-in-nyc-180711162132002](https://user-images.githubusercontent.com/70597605/104543637-e5750f00-55f3-11eb-87c0-2f0bd8612d47.jpg)

# Summary
Analyzed the relationship between average temperature/rainfall and frequency of crime for monthly and quarterly periods in New York City. The result was strong evidence in the relationship between average temperature and frequency of crime, especially assaults. There was evidence of a relationship between average precipitation and frequency of crime, but it was not statistically significant.

### Possible Explanation
The most plausible reason for the relationship between temperature and crime is that warmer weather increases the number of people being outside, which in turn produces more situations for crime to happen.


# Data Sources
*Historical New York City Crime Data - NYPD*
- The New York City Police Department records reported crimes and offense data as required by New York State laws, and is made available for public use. 
- This analysis was done on fifteen years of daily recorded crime, from 2006 to 2020.

*Monthly New York City Climate Summary - NOAA* 
- The National Centers for Environmental Information offers datasets of average monthly climates, which are recorded by various weather stations. The weather station used for this analysis is LaGuardia Airport, which is around eleven miles away from New York City.


# Analysis Method
#### *Hypothesis*
- Warmer temperature causes people to spend more time outside, leading to more chances for criminal activity to take place. As the temperature increases, the frequency of crime will also increase.
- Similarly, as the amount of rainfall increases, the frequency of crimes will lessen.

#### *Null Hypothesis*
- There will be no significant prediction of frequency of crime by average temperature or average rainfall.  

#### *Alternative Hypothesis*
- There is a significant prediction of frequency of crime by average temperature or average rainfall.

#### *Significance Level*
- α = .05


The hypothesis was tested by fitting a Linear Regression line on between our dependent variable (frequency of crime), and independent variable (average temperature or rainfall). 

The following variables were used, totaling four different tests:
1) Average monthly temperature for burglary, assault, and sex crimes
2) Average quarterly temperature  for burglary, assault, and sex crimes
3) Average monthly  precipitation for burglary, assault, and sex crimes
4) Average quarterly precipitation (for burglary, assault, and sex crimes

# Exploratory Data Analysis
![yearly_crime2](https://user-images.githubusercontent.com/70597605/104542100-dfc9fa00-55f0-11eb-8d50-fdde9d792e10.png)
![crime_borough](https://user-images.githubusercontent.com/70597605/104542094-df316380-55f0-11eb-89e1-11bc8d7c746c.png)
![suspect_by_race](https://user-images.githubusercontent.com/70597605/104542095-dfc9fa00-55f0-11eb-8d94-d622eb52eb6a.png)
![ha_crime1](https://user-images.githubusercontent.com/70597605/104542097-dfc9fa00-55f0-11eb-9cc1-1f5fea0621ed.png)


# Average Temperature and Frequency of Crime
### *Results* 
- The analysis provides evidence of a strong relationship between the average precipitation in both quarterly and monthly time periods. 
- The most interesting conclusion is seen from crimes including assault. 
	- Average temperature for monthly periods explains 64% of the variance in the frequency of crimes, and 58% of the variance for quarterly periods. 
- Total crimes and crimes including burglary also show adequate evidence of a relationship. 

The p-value for each of the crimes, especially assault, is extraordinarily small. ***The p-value represents the probability that the null hypothesis is true; in this case, the probability is essentially zero. The p-value is significantly smaller than the significance level of .05, so the null hypothesis is rejected.*** This means the alternative hypothesis is true: as the average temperature rises, so does the frequency of crimes.  


***Regression Analysis of Monthly Periods (Temperature)***

![REgress](https://user-images.githubusercontent.com/70597605/104542410-78607a00-55f1-11eb-82ec-af52d2a9d899.PNG)


***Regression Analysis of Quarterly Periods (Temperature)***

![Capture](https://user-images.githubusercontent.com/70597605/104542540-b65d9e00-55f1-11eb-9fd6-a17715390fc5.PNG)

***Plots (Monthly)***

![freq avg](https://user-images.githubusercontent.com/70597605/104542544-b8bff800-55f1-11eb-8b55-b8dd028a2f06.PNG)

# Average Precipitation and Frequency of Crime
### *Results* 
- Slight negative correlation coefficient between rainfall and the frequency of crime.
- Correlation coefficients for each type of crime for the monthly periods are negative, but the p-values are greater than the significance level of .05, indicating that this is a spurious correlation. 
- Burglary crimes have an extremely high p-value of .715, meaning it is highly unlikely that rainfall has an effect on the frequency of burglaries or robberies. 
- The correlation coefficient for total crime is strong, indicating that there is a relationship between total crime and rainfall during quarterly periods. 
	- The R-squared statistic is .164, and the p-value is .005. , indicating that there is a relationship. 

Excluding total crime for quarterly periods, ***each p-value is over the significance level of .05, so the null hypothesis is rejected in these cases. However, the alternative hypothesis is accepted for total crime over the quarterly period, as it has a p-value of less than .05.*** Rainfall does not have an effect on each of burglary, assault, and sex crimes, however different crimes that are included in total crimes does seem to be effected. The most common crimes that are not one of burglary, assault, or sex crime is marijuana possession and property crimes.

***Regression Analysis of Monthly Periods (Precipitation)***

![yes](https://user-images.githubusercontent.com/70597605/104542545-b9f12500-55f1-11eb-94c8-12d06456a042.PNG)

***Regression Analysis of Quarterly Periods (Precipitation)***

![no](https://user-images.githubusercontent.com/70597605/104542550-bc537f00-55f1-11eb-81b3-de8dcd025187.PNG)

***Plots (Quarterly)***

![bhn](https://user-images.githubusercontent.com/70597605/104542553-be1d4280-55f1-11eb-8835-3c75c4de3446.PNG)
