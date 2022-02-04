from common import db
from sqlalchemy import text

class BModel:
    def __init__(self):
        self.db = db.get_db()

    def get_data(self):
        return self.db.execute(text("""SELECT * FROM table_b""")).fetchone()

    def get_data_many(self):
        return self.db.execute(text("""SELECT * FROM table_b""")).fetchall()