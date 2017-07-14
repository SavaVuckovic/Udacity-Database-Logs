#!/usr/bin/python3.5

'''
This program is created as Udacity Fullstack Developer Nanodegree project
It serves as a reporting tool for the PostgreSQL database that was already
provided by Udacity. It answers each question (ex: What are 3 most popular
articles in the database) using only one SQL query per question.

Author - Sava Vuckovic
'''

import psycopg2

try:
    conn = psycopg2.connect("dbname='news'")
    cursor = conn.cursor()
except Exception as e:
    print(e)

# Three most popular articles
popular_articles = '''
    SELECT
        articles.title,
        COUNT(*)
    FROM log
    JOIN articles
    ON log.path
    LIKE CONCAT('%', articles.slug)
    GROUP BY
        articles.title,
        log.path
    ORDER BY COUNT(*) DESC LIMIT 3;
    '''

# Most popular authors
popular_authors = '''
    SELECT
        name,
        COUNT(*)
    FROM (SELECT *
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path LIKE CONCAT('%', articles.slug))
        AS subquery
    GROUP BY name
    ORDER BY COUNT(*) DESC;
    '''

# Days when more than 1% of requests lead to errors
error_days = '''
    SELECT
        time,
        errors
    FROM (SELECT
            DATE(log.time) AS time,
            ROUND((COUNT(CASE WHEN log.status = '404 NOT FOUND'
            THEN 'x' ELSE NULL END)*100.00)/COUNT('x'), 3) AS errors
        FROM
            log
        GROUP BY DATE(log.time)
        ORDER BY DATE(log.time) DESC)
        AS subquery
    WHERE errors > 1
    LIMIT 5;
    '''


# Query the database, return formatted output
def query(description, sql_query):
    print('\n' + description + '\n')
    try:
        cursor.execute(sql_query)
        result = cursor.fetchall()
        for r in result:
            print('\t', r[0], '---', r[1],
                  'views' if isinstance(r[1], int) else '% errors')
    except Exception as e:
        print('ERROR: ', e)


if __name__ == '__main__':
    query('Top 3 most popular articles are: ', popular_articles)
    query('Most popular article authors are: ', popular_authors)
    query(
        'On following days, more than 1% of requests have lead to errors: ',
        error_days)
