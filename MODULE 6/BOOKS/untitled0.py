import csv
import sqlite3
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# Create an engine to connect to the database
engine = create_engine('sqlite:///books.db')

# Create a metadata object
metadata = MetaData()

# Define a table object to represent the books table
books = Table('books', metadata,
              Column('title', String),
              Column('author', String),
              Column('year', Integer)
             )

# Connect to the database and execute a query to select the title column
with engine.connect() as conn:
    result = conn.execute(books.select().order_by(books.c.title))

    # Print the titles
    for row in result:
        print(row['title'])
