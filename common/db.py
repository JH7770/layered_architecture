from sqlalchemy import create_engine
from flask import current_app, g

def get_db():
    print('get db')
    if 'db' not in g:
        g.db = create_engine(current_app.config['DB_URL'], encoding='utf-8', max_overflow=0)
        print('connect db')
    return g.db


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()
