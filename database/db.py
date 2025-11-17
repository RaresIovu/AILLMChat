import sqlite3
from config import DB_PATH

def get_connection():
    con = sqlite3.connect(DB_PATH)
    # Return rows as tuples (keeping simple). If vrei dicts, adaugă row_factory.
    return con
