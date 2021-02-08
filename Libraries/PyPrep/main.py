import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.feature_selection import chi2
from sklearn.preprocessing import LabelEncoder




class PyPrep:

    def __init__(self, data, copy=True, y=None):
        if copy == True:
            self.data = data.copy()
            if y is not None:
                self.y = data[y]

        else:
            self.data = data
            if y is not None:
                self.y = data[y]

    def head(self):
        return self.data.head()

    def get_numeric(self):
        df_numeric = self.data.select_dtypes(include = [np.number])
        return df_numeric.columns.values


    def get_categorical(self):
        non_numeric = self.data.select_dtypes(exclude = [np.number])
        return non_numeric.columns.values


    def get_missing(self, type = 'list'):
        if type == 'list':
            cols = self.data.columns
            return self.data[cols].isnull().sum()

        if type == 'heatmap':
            fig = plt.figure(figsize=(15, 7))
            cols = self.data.columns
            colors = ['#00FF00', '#FF0000']
            sns.heatmap(self.data[cols].isnull(), cmap=sns.color_palette(colors))
            plt.ylabel('Row Number')
            plt.show()

        if type == 'percentage':
            temp = {}
            for i in self.data.columns:
                pct_missing = np.mean(self.data[i].isnull())
                temp[i] = pct_missing

            temp_df = pd.DataFrame.from_dict(data=temp, orient='index', columns=['Pct'])

            fig = plt.figure(figsize=(10, 15))
            sns.barplot(x='Pct', y=temp_df.index, data=temp_df)
            plt.title('Percentage Missing')
            plt.xlabel('%')
            plt.ylabel('Column')
            plt.show()


    def get_duplicates(self, plot=False):
        if plot == True:
            temp_data = self.data.apply(lambda x : x.duplicated().sum())
            fig = plt.figure(figsize = (10,15))
            sns.barplot(x = temp_data.values, y = temp_data.index)
            plt.xlabel('Number of Duplicates')
            plt.ylabel('Column')
            plt.show()
        else:
            return self.data.apply(lambda x : x.duplicated().sum())

    def get_zscore(self, columns = None, threshold=3):
        if columns is None:
            num_cols = self.get_numeric()
            num = self.data[num_cols]
            mean = np.mean(num)
            std = np.std(num)

            return num[(((num - mean) / std) >= threshold).any(axis=1)]
        else:
            num = self.data[columns]
            mean = np.mean(num)
            std = np.std(num)
            return num[(((num - mean) / std) >= threshold).any(axis=1)]


    def get_repetitive(self, threshold=.95):
        num_rows = len(self.data.index)
        low_info = []
        res = []
        for col in self.data.columns:
            count = self.data[col].value_counts(dropna=False)
            top_pct = (count / num_rows).iloc[0]

            if top_pct > threshold:
                low_info.append(col)
                res.append('{0}: {1:.5f}%'.format(col, top_pct * 100))

    def impute(self, inplace=False, strategy=None, statistics=False):

        if strategy is None:
            imputer = SimpleImputer()
        else:
            imputer = SimpleImputer(strategy=strategy)

        numerics = self.get_numeric()
        num = self.data[numerics]
        imputer.fit(num)
        X = imputer.transform(num)

        if statistics is True:
            print(imputer.statistics_)

        if inplace is True:
            self.data = pd.DataFrame(X, columns = num.columns)
            self.logs[log_num] = ('impute', self.data)
            log_num = log_num + 1
            return self.data
        else:
            data = pd.DataFrame(X, columns = num.columns)
            self.logs[log_num] = ('impute', data)
            log_num = log_num + 1

            return data

    def select_best(self, columns, k=5, dtype='numeric', plot=False):
        if dtype == 'numeric':
            temp = self.data[columns]

            best = SelectKBest(score_func = f_classif, k = k)

            fit = best.fit(temp, self.y)

            scores = pd.DataFrame(fit.scores_)
            pvals = pd.DataFrame(fit.pvalues_)
            cols = pd.DataFrame(columns)
            res = pd.concat([cols, scores, pvals], axis=1)
            res.columns = ['Feature', 'Score', 'Pvalue']

            if plot == False:
                print(res.nlargest(k, 'Score'))
            else:
                fig = plt.figure(figsize = (10,10))
                sns.barplot(x = 'Score', y = 'Feature', data = res)
                plt.show()

        elif dtype == 'categorical':
            temp = self.data[columns]

            best = SelectKBest(score_func=chi2, k=k)

            fit = best.fit(temp, self.y)

            scores = pd.DataFrame(fit.scores_)
            pvals = pd.DataFrame(fit.pvalues_)
            cols = pd.DataFrame(columns)
            res = pd.concat([cols, scores, pvals], axis=1)
            res.columns = ['Feature', 'Score', 'Pvalue']

            if plot == False:
                print(res.nlargest(k, 'Score'))
            else:
                fig = plt.figure(figsize=(10, 10))
                sns.barplot(x='Score', y='Feature', data=res)
                plt.show()

    def corr_plot(self):
        num_cols = self.get_numeric()
        num = self.data[num_cols]
        corr = num.corr()
        mask = np.triu(np.ones_like(corr, dtype=bool))

        fig = plt.figure(figsize = (10,10))
        cmap = sns.diverging_palette(230, 20, as_cmap=True)
        sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0, square=True,
                    linewidths=.5, cbar_kws={'shrink' : .5})
        plt.show()

    def encode(self, columns=None, method='onehot', drop=False):
        if columns is None:
            columns = self.data.columns

        if method == 'onehot':
            dummies = pd.get_dummies(self.data[columns])
            if drop == False:
                self.data = pd.concat([self.data, dummies], axis=1)
            else:
                self.data.drop(columns, axis=1, inplace=True)
                self.data = pd.concat([self.data, dummies], axis=1)

        if method == 'label':
            enc = LabelEncoder()
            encoded = enc.fit_transform(self.data[columns])
            res = pd.DataFrame(encoded, columns=[columns])
            if drop == False:
                self.data = pd.concat([self.data, res], axis=1)
            else:
                self.data.drop(columns, axis=1, inplace=True)
                self.data = pd.concat([self.data, res], axis=1)
