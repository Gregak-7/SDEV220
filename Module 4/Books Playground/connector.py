import sqlite3

# create a connection to the books.db database
conn = sqlite3.connect('books.db')

# create a cursor object
cur = conn.cursor()

# execute a SELECT statement to get the title column in alphabetical order
cur.execute('SELECT title FROM book ORDER BY title')

# loop through the results and print the title column
for row in cur:
    print(row[0])

# close the cursor and connection
cur.close()
conn.close()
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# create an engine that connects to the books.db database
engine = create_engine('sqlite:///books.db', echo=True)

# define metadata and table object
metadata = MetaData()
books = Table('book', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('author', String),
    Column('year', Integer),
)

# create a database connection and execute a SELECT statement to get the title column in alphabetical order
with engine.connect() as conn:
    select_stmt = books.select().order_by(books.c.title)
    result = conn.execute(select_stmt)

    # loop through the results and print the title column
    for row in result:
        print(row['title'])
