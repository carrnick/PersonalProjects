import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import style
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer


class PyNews:

    def __init__(self, key):
        self.key = key
        style.use('ggplot')


    def company_news(self, ticker, size):
        url = "https://seeking-alpha.p.rapidapi.com/news/list"

        querystring = {"id": ticker, "size": size, "until": "0"}

        headers = {
            'x-rapidapi-key': self.key,
            'x-rapidapi-host': "seeking-alpha.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        if response.status_code != 200:
            print('Cannot connect to API. Check the API Key.')


        response = response.json()

        ids = []
        dates = []
        titles = []
        links = []

        for i in response['data']:
            id = i['id']
            date = i['attributes']['publishOn']
            title = i['attributes']['title']
            link =  i['links']['self']

            ids.append(id)
            dates.append(date)
            titles.append(title)
            links.append(link)

        news = News(ids, dates, titles, links, self.key)

        return news

class News(PyNews):
    def __init__(self, ids, dates, titles, links, key):
        temp = {}
        temp['id'] = ids
        temp['date'] = dates
        temp['title'] = titles
        temp['link'] = links

        self.key = key
        self.id = ids
        self.date = dates
        self.title = titles
        self.link = links

        temp_df = pd.DataFrame.from_dict(temp)

        temp_df['date'] = temp_df['date'].apply(lambda x : x.replace('T', ' ')[:16])
        temp_df['date'] = pd.to_datetime(temp_df['date'])

        self.results = temp_df.set_index('date')


    def get_text(self):
        text = []
        for i in self.results['id']:
            url = "https://seeking-alpha.p.rapidapi.com/news/get-details"

            querystring = {"id": i}

            headers = {
                'x-rapidapi-key': self.key,
                'x-rapidapi-host': "seeking-alpha.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            response = response.json()
            content = response['data']['attributes']['content']
            cleaned = re.compile('<.*?>')
            clean_content = re.sub(cleaned, '', content)
            text.append(clean_content)

        self.results['text'] = text
        return text

    def get_sentiment(self):
        analyzer = SentimentIntensityAnalyzer()
        neg = []
        pos = []
        neu = []

        for i in self.results['text']:
            score = analyzer.polarity_scores(i)
            neg.append(score['neg'])
            pos.append(score['pos'])
            neu.append(score['neu'])

        self.results['neg'] = neg
        self.results['pos'] = pos
        self.results['neu'] = neu



    def get_vectorizer(self, range = (1,1), stop_words = True):
        all_text = []
        for i in self.results['text']:
            all_text.append(i)

        if stop_words == False:
            vect = TfidfVectorizer(ngram_range = range)

        else:
            vect = TfidfVectorizer(ngram_range=range, stop_words='english')

        transformed = vect.fit_transform(all_text)

        terms = vect.get_feature_names()
        sums = transformed.sum(axis=0)

        data = []
        for col, term in enumerate(terms):
            data.append((term, sums[0, col]))

        df = pd.DataFrame(data=data, columns=['word', 'count']).sort_values('count', ascending=False)
        return df

    def print_news(self):

        for i, row in self.results.reset_index().iterrows():

            curr_date = row['date']
            curr_title = row['title']

            print('TIME: {}'.format(curr_date))
            print('TITLE: {}'.format(curr_title))
            print('SENTIMENTS (positive, neutral, negative): {}, {}, {}'.format(str(row['pos']), str(row['neu']), str(row['neg'])))
            print()
            print('START TEXT')
            print()
            print(row['text'])
            print()
            print('END TEXT')
            print('-' * 100)
            print()
            print()


    def plot_vocab(self, vocab, num):
        vocab = vocab.head(num)
        fig = plt.figure(figsize = (8,8))
        sns.barplot(x = 'count', y = 'word', data = vocab)
        plt.show()
        
