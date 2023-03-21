import sqlite3
from flask import g

DATABASE = 'test.db'


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# 例外處理


def insert_data(data):
    db = get_db()
    db.cursor().execute("INSERT INTO users VALUES(?, ?)", data)
    db.close()


def query_db(query, args=(), one=False):
    db = get_db().execute(query, args)
    rv = db.fetchall()
    db.close()
    return (rv[0] if rv else None) if one else rv
