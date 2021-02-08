# PyNews

### PyNews is a Python library that is meant to make analyzing financial news easier. Users can search for a company and find the most recent news articles containing that companies ticker, along with sentiment scores and most common words. 

### [Documentation](https://github.com/carrnick/PyNews/blob/main/Documentation.md)

### [Examples](https://github.com/carrnick/PyNews/blob/main/examples.ipynb)

### [Code](https://github.com/carrnick/PyNews/blob/main/PyNews.py)

## Libraries / APIs Used
- [Vader Sentiment](https://pypi.org/project/vaderSentiment/)
- [TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- [Seeking Alpha API](https://rapidapi.com/apidojo/api/seeking-alpha)

## Features
- Allows users to specify a company ticker and total number of articles to return
- Uses [Vader Sentiment](https://pypi.org/project/vaderSentiment/) to analyze and return sentiment scores for each article
- Uses [Sklearn's TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) to find frequency of words for each article
- Prints each articles date of posting, title, sentiment scores, and full text

# Examples / Use Guide

1)  Sign up for an API key on [Rapid API](https://rapidapi.com/apidojo/api/seeking-alpha) to use Seeking Alpha's API service.

2) Import the PyNews library:

`from PyNews import *`


3) Instantiate a PyNews object and enter your API key as a string:

`py = PyNews(key = your_api_key)`

4) Find the ticker for the company to search for and number of articles to return. This example will return the first 10 headlines containing Apple's 
ticker.

`news = py.company_news('aapl', 10)`

The object that is returned can be used in the following ways:

# Result as DataFrame
Accessing the "results" property of the object will return the title, link, text, and sentiment scores of each article.

The columns "pos", "neg", and "neu" are the sentiment scores of the article. `pos` indicates the positivity of the article, `neg` indicates the negativity of the article, and `neu` indicates the neutrality or objectivity of the article.

##### *Code*

`news.results`

##### *Results*

![results](https://user-images.githubusercontent.com/70597605/105081417-29d33580-5a60-11eb-8d6b-0ddb0fd77a70.PNG)

# Word Frequencies

The `get_vectorizer()` method will return a DataFrame of total words and frequencies for the articles.

The "count" column is a statistical measure that evaluates how relavant a word is to a document. The value represents how many times a word appears in a document multiplied by the inverse frequency of the words across the document.

##### *Code*

`news.get_vectorizer()`

##### *Results*

![words](https://user-images.githubusercontent.com/70597605/105081803-ae25b880-5a60-11eb-8a32-2f43b39ade5d.PNG)

# Plotting Word Frequencies

To plot words and frequencies that is returned by `get_vectorizer()`, use `plot_vocab(vocab, number)`.

The `number` parameter is the amount of words to plot. For example, specifying `number` as 15 will plot the words with the 15 highest frequencies.


##### *Code*

`news.plot_vocab(vocab, 15)`

##### *Results*

![plot](https://user-images.githubusercontent.com/70597605/105082069-0bba0500-5a61-11eb-9ccb-d80b37d5ce28.PNG)


# Full Text and Sentiment Scores

To read each articles text and sentiment scores, use the `print_news()` function. This will print each articles time of posting, title, sentiment scores, and full text.

##### *Code*

`news.print_news()`

##### *Results*

![asd](https://user-images.githubusercontent.com/70597605/105082324-62274380-5a61-11eb-8b56-bab7705b706f.PNG)




