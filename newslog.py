#! /usr/bin/env python


"""This is a log analysis tool for the news database"""


import psycopg2
from datetime import datetime


def get_article_leaderboard():
    """What are the most popular three articles of all time? """
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    columns_descr = c.description
    c.execute("select * from article_leaderboard")
    result_articles = c.fetchall()
    for row in result_articles:
        x, y = row
        print('Article: ' + '%s' % (x) + ' - Views: ' + '%s' % (y))
    db.close()


def get_author_leaderboard():
    """Who are the most popular article authors of all time?"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    columns_descr = c.description
    c.execute("select * from author_leaderboard;")
    result_authors = c.fetchall()
    for row in result_authors:
        x, y = row
        print('Author: ' + '%s' % (x) + ' - Views: ' + '%s' % (y))
    db.close()


def get_bad_days():
    """On which days did more than 1% of requests lead to errors?"""
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    columns_descr = c.description
    c.execute("select * from bad_days;")
    result_days = c.fetchall()
    for row in result_days:
        x, y = row
        oldformat = str(x)
        datetimeobject = datetime.strptime(oldformat, '%Y-%m-%d')
        newformat = datetimeobject.strftime('%B %d, %Y')
        x = newformat
        print('Date: ' + '%s' % (x) + ' - Error Percentage: ' + '%s' % (y))
    db.close()

# Print the output of the database analysis
print("What are the most popular three articles of all time?" + '\n')
get_article_leaderboard()
print('\n')
print("Who are the most popular article authors of all time?" + '\n')
get_author_leaderboard()
print('\n')
print("On which days did more than 1% of requests lead to errors?" + '\n')
get_bad_days()
