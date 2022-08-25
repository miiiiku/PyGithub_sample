import os

import now as now
from github import Github
import pandas as pd
import datetime
from tqdm import tqdm
import time
import seaborn as sns
import matplotlib.pyplot as plt

token = "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"
df = pd.DataFrame(columns=['stars', 'language', 'topics', 'days', 'forks_count'])
df_language = pd.DataFrame(columns=['language'])
language = set()

dt_now = datetime.datetime.now()
g = Github(token)

repositories = g.search_repositories(query='stars:9500<10000', sort='stars', order='desc')

# Then play with your Github objects:

for repo in repositories:
    days = dt_now - repo.created_at
    # readme_size = repo.get_readme().size
    language.add(str(repo.language))

    df = pd.concat([df, pd.DataFrame(
        data=[[repo.stargazers_count, repo.language, len(repo.get_topics()), days.days,
               repo.forks_count]], columns=['stars', 'language', 'topics', 'days', 'forks_count'],
        index=[repo.name])])
    print(df)

df = pd.get_dummies(df, columns=['language'])
# df.drop('language', axis=1)


colormap = plt.cm.RdBu
plt.figure(figsize=(14, 12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(df.astype(float).corr(), linewidths=0.1, vmax=1.0,
            square=True, cmap=colormap, linecolor='white', annot=True)
plt.savefig('heatmap_list9500-10000.png')
res = df.corr()

sns.boxplot(data=res)
plt.savefig('hako9500-10000.png')

df.to_csv("sample.csv", index=True)
