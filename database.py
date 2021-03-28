import sqlite3
create_article_table = "CREATE TABLE IF NOT EXISTS articles( title TEXT,  articledate TEXT , content TEXT)"
create_article = "INSERT INTO articles VALUES (? , ? , ?)"
retrieve_articles = "SELECT * FROM articles"
#connection =  sqlite3.connect("data.db")

def fn_create_article_table():
    with sqlite3.connect("data.db") as connection:
        connection.execute(create_article_table)

def fn_create_article(title, articledate , content):
    with sqlite3.connect("data.db") as connection:
        connection.execute(create_article,(title, articledate , content))

def fn_retrieve_articles():
    with sqlite3.connect("data.db") as connection:
        cursor = connection.cursor()
        cursor.execute(retrieve_articles)
        return cursor.fetchall()
        