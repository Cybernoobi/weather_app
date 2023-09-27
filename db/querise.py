from .base import connect_db, commit_and_close


def check_user_exists(db_name: str, username: str):
    conn, cursor = connect_db(db_name)
    cursor.execute('SELECT * FROM users WHERE username = ?;', (username,))
    user = cursor.fetchone()
    return True if user else False


def add_user(db_name: str, username: str):
    conn, cursor = connect_db(db_name)
    cursor.execute('INSERT INTO users(username) VALUES (?);', (username,))
    commit_and_close(conn)

    print('user added: ', username)

