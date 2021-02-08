

# Creating PyNews Object
**Method:** `PyNews(key)`

***Parameters:***
- `key`: String of API Key from [Rapid API](https://rapidapi.com/apidojo/api/seeking-alpha)

***Returns:*** 
- PyNews object

# Getting Company News

**Method:**  `company_news(ticker, size)`

***Parameters:***
- `ticker`: String representing ticker symbol of a company 
- `size`: Integer representing how many articles to return

***Returns:*** 
- News object that contains:
	- `ids`: list of article IDs
	- `date`: list of article dates
	- `title`: list of article titles
	- `link`: list of article links
	- `results`: DataFrame of article dates, titles, link, and texts 

# Getting Word Frequencies
**Method:** `get_vectorizer(range = (1,1) , stop_words = True)`

***Parameters:***
- `range`: Tuple of integers representing the range of words to find. Default is `(1,1)`, meaning only single words will be returned.
- `stop_words`: Boolean value. If True, common English words such as "the, is, in, as" etc. will be ignored while finding frequencies of words.

***Returns:*** 
	- `DataFrame`: a Pandas DataFrame containing each word and frequency
	
# Plotting Word Frequencies
**Method:** `News.plot_vocab(vocab, number)`

***Parameters:***
- `vocab`: Pandas DataFrame containing words and frequencies. Use the value returned by `get_vectorizer`
- `number`: Integer specifying the amount of words to plot

# Full Text and Sentiment Scores
**Method:** `News.print_news()`

