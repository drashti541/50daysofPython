#Task 1:  Create a DataFrame
print("\n*******************Task 1:  Create a DataFrame*******************")
import pandas as pd
table = {'year': [2009, 2002, 2009, 2010, 2009],
 'title': ["Brothers", "Spider-Man", "WatchMen", "Inception", "Avatar"],
 'genre': ["Drama", "Sci-fi", "Drama", "Sci-fi", "Fantasy"]}
movies = pd.DataFrame(table)
print(movies)



#Task 2:  Website Data with Pandas
print("\n*******************Task 1:  Website Data with Pandas*******************")
web = pd.read_html("https://en.wikipedia.org/wiki/Python_(programming_language)")

print(web[1])
print(web[1][['Type', 'Mutability']])
