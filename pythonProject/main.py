import numpy as np
import matplotlib.pyplot as plt
from github import Github
from matplotlib import ticker

token = "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"

g = Github(token)
data_size = []
data_name = []

repositories = g.search_repositories(query="size:>100000000", order="desc")
repositories = list(repositories)
repositories = sorted(repositories, key=lambda x: x.size, reverse=True)

for repo in repositories[0:5]:
    data_size.append(repo.size)
    data_name.append(repo.name)
    print(repo.size)

plt.bar(data_name, data_size)

# after plotting the data, format the labels
current_values = plt.gca().get_yticks()
# using format string '{:.0f}' here but you can choose others
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])
plt.xlabel('repo_name')
plt.ylabel('repo.size')
plt.title('top 5 of size')
plt.show()
