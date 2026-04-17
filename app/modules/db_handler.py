
import sqlite3
from config.config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS cache (id INTEGER PRIMARY KEY AUTOINCREMENT, data TEXT)")
    conn.commit()
    conn.close()

def insert_data(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cache (data) VALUES (?)", (data,))
    conn.commit()
    conn.close()

def fetch_data(limit=10):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, data FROM cache ORDER BY id ASC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_data(ids):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executemany("DELETE FROM cache WHERE id = ?", [(i,) for i in ids])
    conn.commit()
    conn.close()
