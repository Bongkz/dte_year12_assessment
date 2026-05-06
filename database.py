import sqlite3
from flask import g

# Database file name
DATABASE = "database.db"

# Creates a database connection
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

# Closes the database connection
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
