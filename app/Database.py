# -*- coding: utf-8 -*-

import sqlite3

class Database:

    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
    
    def select_story_id(self, story_id):
        with self.conn:
            return self.cursor.execute('SELECT id from hackernews WHERE id=?', (story_id,)).fetchone()[0]
    def select_all_news(self):
        with self.conn:
            return self.cursor.execute('SELECT * FROM hackernews').fetchall()
    def select_category(self, category):
        with self.conn:
            return self.cursor.execute('SELECT * FROM hackernews WHERE category=?', category)
    def insert_news(self, news):
        query = "INSERT INTO hackernews(id, title, type, url, category) VALUES(?,?,?,?,?)"
        with self.conn:
            self.cursor.execute(query, news)
    
    def close(self):
        self.conn.close()