# **Strength in Numbers**

## *WallStreetBets Sentiment Analysis*

Reddit is a social media platform that allows users to create "subreddits", which are communities usually centered around a single topic. The individuals in the subreddit are able to submit content in the form of text, links, or images, which are then upvoted or downvoted by the other members. 



Reddit was the center of the financial news world in early 2021, as members of the WallStreetBets subreddit coordinated to drive up the prices of stocks like Gamestop and AMC. The goal of the subreddit was to take advantage of large hedge funds that "shorted" stocks, or bet against them going down. The plan was to get the members of the WallStreetBets community, which has around 3 million members, to buy stock in companies that were shorted by the hedge fund owners. This drove the price up, forcing the hedge fund owners to buy back stock, which even further increased the price. Gamestop's stock price rose by as much as 1,800% in only a week, which was the result of the WallStreetBets community reluctance to sell and determiniation to "hold the line".

The WallStreetBets subreddit acted as the headquarters for coordinating and executing a massive market movement against wealthy hedge fund owners. By using Python's sentiment analysis libraries, we can get a better idea of what was being said and of the underlying emotions in the posts. 



# Libraries Used 

- [vaderSentiment](https://pypi.org/project/vaderSentiment/) 
- [Spacy](https://spacy.io/)
- [text2emotion](https://pypi.org/project/text2emotion/)
- [Nltk](https://www.nltk.org/)



# Results 

### Frequently Mentioned Organizations and Sentiment

![organization_sentiments](https://user-images.githubusercontent.com/70597605/107979493-a3414380-6f8c-11eb-812e-a2945feaba85.png)

![most_common_orgs](https://user-images.githubusercontent.com/70597605/107979476-9f152600-6f8c-11eb-9d81-d9f50b13b9b1.png)

### Most Common Words in Title and Body

![most_common_words_title](https://user-images.githubusercontent.com/70597605/107979488-a2a8ad00-6f8c-11eb-82dd-b7e158bf62f9.png)

![most_common_words_body](https://user-images.githubusercontent.com/70597605/107979478-9f152600-6f8c-11eb-9d72-8f8f3fefdda4.png)

### Distribution of Word Counts in Title and Body

![dist_word_counts](https://user-images.githubusercontent.com/70597605/107979474-9f152600-6f8c-11eb-85bc-b9c653e7a3e7.png)

### Number of Posts and Comments per Day

![num_posts_day](https://user-images.githubusercontent.com/70597605/107979491-a2a8ad00-6f8c-11eb-95d1-13696cf6202e.png)

![num_comments_day](https://user-images.githubusercontent.com/70597605/107979489-a2a8ad00-6f8c-11eb-9b4c-7cb09b95f878.png)


### What Happened on January 29?

January 29, 2021 was a day of extreme volatility on the stock market, and was the day WallStreetBets was most active.

[A total of 19.58 billion shares were traded on Thursday, higher than the last 20-session average of 14.86 billion.](https://finance.yahoo.com/news/stock-market-news-jan-29-143602336.html#:~:text=A%20total%20of%2019.58%20billion,1%20ratio%20favored%20advancing%20issues.)

![num_posts_jan29](https://user-images.githubusercontent.com/70597605/107979492-a2a8ad00-6f8c-11eb-9da1-4818e5e1850e.png)

![most_common_words_jan29](https://user-images.githubusercontent.com/70597605/107979480-9f152600-6f8c-11eb-9cef-5e4204d94161.png)

### Distribution of Sentiments (20 minute interval)

![sentiment20min](https://user-images.githubusercontent.com/70597605/107979505-a76d6100-6f8c-11eb-92bc-242cd456eb96.png)

![sentiment20min_pctchange](https://user-images.githubusercontent.com/70597605/107979502-a6d4ca80-6f8c-11eb-8b35-5e9d61881b3d.png)

### Distribution of Sentiments (Hourly interval)



![sentimenthour](https://user-images.githubusercontent.com/70597605/107979509-a76d6100-6f8c-11eb-89da-6d70e335eb5e.png)

![sentimenthour_pct](https://user-images.githubusercontent.com/70597605/107979508-a76d6100-6f8c-11eb-9f2b-65434fbd589d.png)


### Distribution of Sentiments (Daily interval)

![sentiment_day](https://user-images.githubusercontent.com/70597605/107979494-a50b0700-6f8c-11eb-9aee-91038e8c14f9.png)

![sentimentday_pct](https://user-images.githubusercontent.com/70597605/107979506-a76d6100-6f8c-11eb-9d93-cc9ec2380965.png)

### Emotion of Posts 

![emotion](https://user-images.githubusercontent.com/70597605/107979475-9f152600-6f8c-11eb-8c82-bcde476650de.png)



### Correlation Matrix 

![corr](https://user-images.githubusercontent.com/70597605/107979473-9e7c8f80-6f8c-11eb-9c73-e2a77a156a22.png)
