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

![organization_sentiments](/Users/nickcarrolli/Desktop/Data Science/WallStBets/organization_sentiments.png)

![most_common_orgs](/Users/nickcarrolli/Desktop/Data Science/WallStBets/most_common_orgs.png)

### Most Common Words in Title and Body

![most_common_words_title](/Users/nickcarrolli/Desktop/Data Science/WallStBets/most_common_words_title.png)

![most_common_words_body](/Users/nickcarrolli/Desktop/Data Science/WallStBets/most_common_words_body.png)

### Distribution of Word Counts in Title and Body

![dist_word_counts](/Users/nickcarrolli/Desktop/Data Science/WallStBets/dist_word_counts.png)

### Number of Posts and Comments per Day

![num_posts_day](/Users/nickcarrolli/Desktop/Data Science/WallStBets/num_posts_day.png)

![num_comments_day](/Users/nickcarrolli/Desktop/Data Science/WallStBets/num_comments_day.png)



### What Happened on January 29?

January 29, 2021 was a day of extreme volatility on the stock market, and was the day WallStreetBets was most active.

[A total of 19.58 billion shares were traded on Thursday, higher than the last 20-session average of 14.86 billion.](https://finance.yahoo.com/news/stock-market-news-jan-29-143602336.html#:~:text=A%20total%20of%2019.58%20billion,1%20ratio%20favored%20advancing%20issues.)

![num_posts_jan29](/Users/nickcarrolli/Desktop/Data Science/WallStBets/num_posts_jan29.png)

![most_common_words_jan29](/Users/nickcarrolli/Desktop/Data Science/WallStBets/most_common_words_jan29.png)

### Distribution of Sentiments (20 minute interval)

![sentiment20min](/Users/nickcarrolli/Desktop/Data Science/WallStBets/sentiment20min.png)

![sentiment20min_pctchange](/Users/nickcarrolli/Desktop/Data Science/WallStBets/sentiment20min_pctchange.png)

### Distribution of Sentiments (Hourly interval)



![sentimenthour_pct](/Users/nickcarrolli/Desktop/Data Science/WallStBets/sentimenthour.png)![sentimenthour_pct](/Users/nickcarrolli/Desktop/Data Science/WallStBets/sentimenthour_pct.png)



### Distribution of Sentiments (Daily interval)

![sentiment_day](/Users/nickcarrolli/Desktop/Data Science/WallStBets/sentiment_day.png)

### ![sentimentday_pct](/Users/nickcarrolli/Desktop/Data Science/WallStBets/sentimentday_pct.png)

### Emotion of Posts 

![emotion](/Users/nickcarrolli/Desktop/Data Science/WallStBets/emotion.png)



### Correlation Matrix 

![corr](/Users/nickcarrolli/Desktop/Data Science/WallStBets/corr.png)
