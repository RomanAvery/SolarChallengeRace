import os
import sqlite3

cur_dir = os.path.dirname(os.path.realpath(__file__))

class Database:
    def __init__(self, filename="solar.db"):
        self.conn = sqlite3.connect(cur_dir + '/' + filename, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Create table if it doesn't exist
        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS teams
            (
                ID  INTEGER PRIMARY KEY NOT NULL,
                BARCODE TEXT    NOT NULL,
                NAME    TEXT    NOT NULL
            );
        ''')

        self.cur.execute('''
            CREATE TABLE IF NOT EXISTS races
            (
                ID  INTEGER PRIMARY KEY NOT NULL,
                TEAMONE INTEGER NOT NULL,
                TEAMTWO INTEGER NOT NULL,
                TIME    INTEGER,
                WINNERID  INTEGER
            )
        ''')

        self.conn.commit()