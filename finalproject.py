import pandas as pd
import matplotlib.pyplot as plt

url = 'https://en.wikipedia.org/wiki/The_Legend_of_Zelda'
df = pd.read_html(url, match="Release timeline")[0]

df = df.rename(columns={0: 'Year'})
df['Year'] = df['Year'].astype(str).str.extract('(\d+)', expand=False).astype(int)

numeric_cols = df.select_dtypes(include='number').columns.tolist()
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['Year'], df[numeric_cols])
ax.set_xticks(df['Year'])
ax.set_xlim(left=1985, right=2022)
ax.set_xlabel('Year')
ax.set_ylabel('Number of Games')
ax.set_title('The Legend of Zelda Release Timeline')
plt.show()