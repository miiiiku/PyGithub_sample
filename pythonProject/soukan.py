import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('sample.csv')
res = df.corr()

res.to_csv("soukan.csv", index=True)
print(res)
