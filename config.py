db = {
    'user': 'root',
    'password': 'ansdjdhkd1',
    'host': 'localhost',
    'port': 3306,
    'database': 'test'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
