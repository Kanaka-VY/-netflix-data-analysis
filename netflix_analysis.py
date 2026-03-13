import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("netflix_titles.csv")

# Show first rows
print(data.head())

# Movies vs TV Shows
type_count = data['type'].value_counts()

plt.figure(figsize=(6,4))
sns.barplot(x=type_count.index, y=type_count.values)
plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

# Release year trend
year_data = data['release_year'].value_counts().sort_index()

plt.figure(figsize=(10,5))
year_data.plot()
plt.title("Content Release Over Years")
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

# Top countries producing Netflix content
top_countries = data['country'].value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_countries.values, y=top_countries.index)

plt.title("Top 10 Countries Producing Netflix Content")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.show()


# Top genres
top_genres = data['listed_in'].str.split(', ').explode().value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=top_genres.values, y=top_genres.index)

plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")

plt.show()
