import sqlite3


def connect_db(db_name: str):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor


def commit_and_close(connection: sqlite3.Connection):
    connection.commit()
    connection.close()
