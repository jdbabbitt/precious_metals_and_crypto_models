import quandl
import pandas as pd
import matplotlib.pyplot as plt

df = quandl.get("AAII/AAII_SENTIMENT")
df = df.iloc[-1,0:3]
labels = df.index
colors = ['limegreen', 'skyblue','red']
plt.pie(df, colors=colors,
            autopct='%1.1f%%',
            shadow=True,
            labels = labels,
            wedgeprops={'edgecolor': 'white'})
plt.title('Investor Sentiment')

plt.show()
