from common import db
from sqlalchemy import text

class AModel:
    def __init__(self):
        self.db = db.get_db()

    def get_data(self):
        return self.db.execute(text("""SELECT * FROM table_a""")).fetchone()

    def get_data_many(self):
        return self.db.execute(text("""SELECT * FROM table_a""")).fetchall()