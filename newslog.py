"""This is a log analysis tool for the news database"""

import datetime
import psycopg2

def get_article_leaderboard():
  """What are the most popular three articles of all time? """
  db = psycopg2.connect("dbname=news")
  c = db.cursor()
  c.execute("select * from article_leaderboard")
  return c.fetchall()
  db.close()

def get_author_leaderboard():
  """Who are the most popular article authors of all time?"""
  db = psycopg2.connect("dbname=news")
  c = db.cursor()
  c.execute("select * from author_leaderboard;")
  return c.fetchall()
  db.close()
  
def get_bad_days():
  """On which days did more than 1% of requests lead to errors?"""
  db = psycopg2.connect("dbname=news")
  c = db.cursor()
  c.execute("select * from bad_days;")
  return c.fetchall()
  db.close()  
  
# Print the output of the database analysis
print(get_article_leaderboard())
 
print(get_author_leaderboard())
 
print(get_bad_days())


