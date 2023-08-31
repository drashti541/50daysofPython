#Task 1:  Create a Database
print("\n*******************Task 1:  Create a Database*******************")
import sqlite3

con = sqlite3.connect("movies.db")
cur = con.cursor()

# cur.execute("CREATE TABLE movies(year, title, genre)")

movies =  [
    (2009, 'Brothers', 'Drama'),
    (2002, 'Spider-Man', 'Sci-fi'),
    (2009, 'WatchMen', 'Drama'),
    (2010, 'Inception', 'Sci-fi'),
    (2009, 'Avatar', 'Fantasy')
    ]

cur.executemany("INSERT INTO movies VALUES(?, ?, ?);", movies)
row = cur.fetchall()
for row in cur.execute('SELECT * FROM movies;'):
    print(row)

print()    
row = cur.fetchall()
for row in cur.execute('SELECT * FROM movies where "title"="Brothers";'):
    print(row)

# cur.execute("DROP TABLE movies")    
con.commit()
con.close()